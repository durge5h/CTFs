from itertools import cycle

def xor_decrypt(encrypted_data, key):
    return [i ^ j for i, j in zip(encrypted_data, cycle(key))]

enc_data = open("enc.txt", "rb").read()
key = [enc_data[0], enc_data[1], enc_data[2], enc_data[3], enc_data[4], enc_data[5], enc_data[6], enc_data[7]]

decrypted_data = bytearray(xor_decrypt(enc_data, key))

with open("decrypted_image.png", "wb") as f:
    f.write(decrypted_data)
