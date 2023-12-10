#!/usr/bin/env python3

from pwn import *

exe = ELF("./random")

context.binary = exe


def conn():
    r = process([exe.path])
    return r


def main():
    #r = remote("challs.tfcctf.com", 31600)
    r = conn() 
    payload = process("./helper").read()
    print(payload)
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    main()
