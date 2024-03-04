def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]

def xor_decrypt(encrypted_data, key):
    decrypted = bytearray(xor(encrypted_data, key))
    return decrypted

# Read the encrypted file
encrypted_data = open('enc.txt', 'rb').read()

# Extract the key from the encrypted data
key = encrypted_data[:8]

# Decrypt the data
decrypted_data = xor_decrypt(key,encrypted_data)

# Write the decrypted data back to an image file
open('decrypted_image.png', 'wb').write(decrypted_data)
