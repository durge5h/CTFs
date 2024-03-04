from itertools import cycle

with open("enc.txt", "rb") as f:
    encrypted_data = f.read()

key = encrypted_data[:8]
decrypted_data = bytearray(i ^ j for i, j in zip(encrypted_data, cycle(key)))

with open("decrypted.png", "wb") as f:
    f.write(decrypted_data)
