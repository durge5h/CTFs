#!/usr/bin/env python3

from pwn import *
import time

exe = ELF("./pse")
context.log_level = 'info'
context.binary = exe
cc = ''

def conn():
    #r = remote('92.246.89.201',10001)
    r = process([exe.path])
    return r

num2choice = lambda num: 'Espresso' if num == b'0' else ('Spaghetti' if num == b'1' else 'Pizza')

def main():
    #r = remote("challs.tfcctf.com", 31600)
    r = conn()
    while True:
        for _ in range(10):
            num = process("./helper2").read()
            # num = int([num.strip() for num in nums])
            print(f"nums : {num},{type(num)}")
            res = num2choice(num)
            print(res)
            r.recvuntil('>> ')
            r.sendline(res)
        r.recvuntil("WIN RATE")
        res2 = r.recv(20).strip()
        info(f"Score :{res2}")
        if b"10/10" in res2:
            success("Found!!!")
            r.interactive()
        else:
            #r = remote('92.246.89.201',10001)
            r = process([exe.path])

if __name__ == "__main__":
    main()
