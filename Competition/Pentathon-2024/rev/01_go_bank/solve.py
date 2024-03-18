#!/usr/bin/env python3

from pwn import *

elf = ELF("./bank")
libc = elf.libc

context.binary = elf
context.log_level = 'info'

gdbscript='''
'''

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

def brute(r,payload):
        # r.recvuntil(b"your option > ")
        # r.sendline(str(payload))
        r.sendlineafter(b"your option > ",b'5')
        r.sendlineafter(b"Enter Varun's account number to get the flag: ",str(payload))
        # temp_flag = r.recvline().split(b':')[1].strip()
        # print(hex(unpack(temp_flag,'all')))
        # exit()

        rsp = r.recvline(3)
        print(r.recvline(3))

        with open('result.txt','ab') as f:
            # print(f"rsp : {rsp}")
            f.write(rsp)

        # print(int(hex(unpack(r.recvline(3).strip(),'all'))),16)
        # print(temp_flag)
        # print(r.recvline(3))
        # if b'Here is your flag:' in resp:
        #     print(resp)
        #     exit()

def main():
    r = conn()
    for i in range(2222222222,3333333333):
        print(f"i: {i}")
        brute(r,i)
    # brute(r,2222232870)
    # r.interactive()


if __name__ == "__main__":
    main()

