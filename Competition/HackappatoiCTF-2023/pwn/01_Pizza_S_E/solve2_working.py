from ctypes import CDLL
import time
from pwn import *

def generate_random(size):
    libc = CDLL(None)
    libc.srand(int(time.time()))

    random = []
    for j in range(size):
        randnum = libc.rand() % 3
        random.append(randnum)
    return random

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

exe = './pse'
elf = context.binary = ELF(exe, checksec=False)

# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

io = start()

winrate = 0
value = generate_random(10)
for i in range(10):
    if value[winrate] == 0:
        io.sendlineafter(b'>>', 'Espresso')
        winrate += 1
    elif value[winrate] == 1:
        io.sendlineafter(b'>>', 'Spaghetti')
        winrate += 1
    else:
        io.sendlineafter(b'>>', 'Pizza')
        winrate += 1

io.interactive()
