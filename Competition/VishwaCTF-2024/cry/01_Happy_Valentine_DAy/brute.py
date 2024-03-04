from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

enc = open("enc.txt", "rb").read()

# Brute-force the key
for i in range(256):
    for j in range(256):
        for k in range(256):
            for l in range(256):
                for m in range(256):
                    for n in range(256):
                        for o in range(256):
                            for p in range(256):
                                key = [i, j, k, l, m, n, o, p]
                                dec = bytes(xor(enc, key))
                                # Check if the decryption result is a valid image
                                try:
                                    Image.open(io.BytesIO(dec))
                                    print("Found potential key:", key)
                                    # If you find a potential key, you can stop the brute-force
                                    # attack and use this key to decrypt the file
                                    break
                                except:
                                    pass
