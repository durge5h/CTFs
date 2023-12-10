import ctypes
import random
from pwn import *

# Load the C library (libc) using ctypes
libc = ctypes.CDLL(None)

# Define the return types of the C functions
libc.time.restype = ctypes.c_long
libc.srand.argtypes = [ctypes.c_uint]
libc.rand.restype = ctypes.c_int

# Equivalent C code snippet
# tVar2 = time((time_t *)0x0);
tVar2 = libc.time(0)

# srand((uint)tVar2);
libc.srand(ctypes.c_uint(tVar2))

# Initialize an array to store the random values
v = (ctypes.c_int * 10)()

elf = context.binary = ELF('./random')

r = process()
#r = remote('challs.tfcctf.com',31558)
# for (i = 0; i < 10; i = i + 1) {
r.recvuntil(b"numbers!\n")
for i in range(10):
    # iVar1 = rand();
    iVar1 = libc.rand()
    # *(int *)(v + (long)i * 4) = iVar1;
    v[i] = iVar1
    
    print(v[i])
    r.sendline(str(v[i])) 

'''
for i in range(10):
    print(str(v[i]))
    r.sendline(str(v[i]))
'''
r.interactive() 

