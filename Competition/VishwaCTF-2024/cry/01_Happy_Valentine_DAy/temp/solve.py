from itertools import cycle

with open("enc.txt", "rb") as f:
    encrypted_data = f.read()

# Try identifying image format (replace with your preferred detection method)
possible_format = "PNG"  # Replace with detected format if possible

# Extract a potential key (might need adjustment based on format analysis)
key = encrypted_data[:8]

decrypted_data = bytearray(i ^ j for i, j in zip(encrypted_data, cycle(key)))

with open(f"decrypted.{possible_format}", "wb") as f:
    f.write(decrypted_data)
