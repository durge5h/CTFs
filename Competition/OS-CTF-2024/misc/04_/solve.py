import socket
import hashlib
import itertools
import string

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def brute_force_hidden_chars(pattern, target_hash):
    chars_to_try = string.ascii_letters + string.digits
    hidden_positions = [i for i, char in enumerate(pattern) if char == '*']
    num_hidden = len(hidden_positions)

    for guess in itertools.product(chars_to_try, repeat=num_hidden):
        candidate = list(pattern)
        for pos, char in zip(hidden_positions, guess):
            candidate[pos] = char
        candidate_str = ''.join(candidate)
        if md5_hash(candidate_str) == target_hash:
            return ''.join(guess)

    return None

def main():
    host = '34.16.207.52'
    port = 5664

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        while True:
            data = s.recv(1024).decode().strip()
            print(data)

            if "Find the hidden characters" in data:
                pattern_line = s.recv(1024).decode().strip()
                pattern, target_hash = pattern_line.split(' -> ')
                target_hash = target_hash.strip()

                hidden_chars = brute_force_hidden_chars(pattern, target_hash)
                if hidden_chars:
                    print(f"Hidden characters found: {hidden_chars}")
                    s.sendall((hidden_chars + "\n").encode())
                else:
                    print("Failed to find hidden characters.")
                    break

            elif "Incorrect!" in data:
                print("Incorrect answer. Try again.")
                break

            if "FLAG" in data:
                print("FLAG found!")
                break

if __name__ == "__main__":
    main()
