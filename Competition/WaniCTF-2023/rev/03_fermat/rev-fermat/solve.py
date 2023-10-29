def print_flag():
    local_b8 = [0xf781fc86, 0xc5afc9bb, 0xd5a5de9f, 0xefa1efa4, 0xefb4dfac,
                0xc49fd6af, 0xefa5dda9, 0xefa4dea1, 0xdfa6d6a5, 0xc49fc4b2,
                0xdfb3efaf, 0xefa5c6ac, 0xd5b6d5b2, 0xdea9c3b2, 0x80f2efa7,
                0x87f4d2f8, 0x86f6d4a2, 0xd4a382a3, 0xb0c0cdf8]

    local_68 = bytearray(0 for i in range(0, 80))

    for local_bc in range(0, 0x13):
        local_68[local_bc*4] = local_b8[local_bc] & 0xff ^ 0xc0
        local_68[local_bc*4+1] = (local_b8[local_bc] >> 8) & 0xff ^ 0xb0
        local_68[local_bc*4+2] = (local_b8[local_bc] >> 16) & 0xff ^ 0xc0
        local_68[local_bc*4+3] = (local_b8[local_bc] >> 24) & 0xff ^ 0xb0

    print(local_68.decode())

print_flag() 
