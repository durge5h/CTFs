import os
import binascii
import struct

misc = open("chall.png","rb").read()

for i in range(1024):
    data = misc[12:16] + struct.pack('>i',i)+ misc[16:20]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0xcda0e401:
        print(i)
