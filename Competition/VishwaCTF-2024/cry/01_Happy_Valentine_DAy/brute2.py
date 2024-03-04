from itertools import cycle

def xor(data, key):
  """Performs XOR operation between data and a cyclic key."""
  return bytearray(i ^ j for i, j in zip(data, cycle(key)))

def try_key_length(data, key_length):
  """Attempts decryption with different keys of the given length."""
  for i in range(256**key_length):
    key = bytes([i // (256**j) % 256 for j in range(key_length)])
    decrypted = xor(data, key)
    # You can add checks here to see if the decrypted data resembles an image
    # based on your knowledge of the format (e.g., header bytes, size)
    # Implement your specific checks here
    # if is_valid_image(decrypted):
    #   return key, decrypted
  return None, None

def main():
  with open("enc.txt", "rb") as f:
    data = f.read()

  # Try different key lengths based on your assumptions (adjust as needed)
  for key_length in [1, 2, 4, 8]:  # Adjust based on your assumptions
    key, decrypted = try_key_length(data, key_length)
    if key:
      print(f"Found key: {key.hex()}")
      # Save the decrypted data with an appropriate extension (if valid)
      # with open(f"decrypted.{possible_format}", "wb") as f:
      #   f.write(decrypted)
      break

if __name__ == "__main__":
  main()
