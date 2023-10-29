from pwn import *
import re,os

#r = remote("netcat-pwn.wanictf.org",9001)
elf = context.binary = ELF("./chall")
context.log_level = "info" 


#r = process() 
r = remote("netcat-pwn.wanictf.org",9001)

for i in range(5):
    try:
        r.recvline()
        r.recvline()
        data = r.recv().decode()
        print(data)
        equ = re.search(r"\d+\s*\+\s*\d+",data) 

        print("equ :",equ)
        #equ = equ.group() 
        
        ans = eval(str(equ.group()))
        print("ans : ",ans)

        r.sendline(str(ans).encode())

    except:
        r.interactive() 

