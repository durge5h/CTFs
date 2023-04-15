#!/usr/bin/env python

from pwn import *
import os

p = remote('64.227.41.83',30145)
p.sendline("1")
info("Wait till you get the flag :) ")
for i in range(100):
	step = 100-i
	print("{} step closer to your flag".format(step))
	#recieve input interface
	p.recv()
	#time.sleep(1)
	p.sendline("rockpaperscissors")

p.recvuntil('prize: ')
flag = p.recv()
os.system("clear")
success("\n\n\tflag : {}".format(flag))
#p.interactive()
