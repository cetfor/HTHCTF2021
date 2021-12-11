#!/usr/bin/env python3

import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Crypto facilities from pycryptodome: `pip3 install pycryptodome`
# https://www.pycryptodome.org/en/latest/src/installation.html
# Credit: http://aes.cryptohack.org/ecb_oracle/

KEY = b"ThisIsAK3yW0w!!1" # length: 16-bytes, 128-bits
FLAG = "HTH{f14g_leak}"   # length: 14-bytes

def read_file(file_name):
    f = open(file_name, "r")
    flag = f.read()
    f.close()
    return flag

def encrypt(plaintext):
    plaintext = bytes(plaintext, encoding='utf8')
    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return json.dumps({"ciphertext": encrypted.hex()})

def main():
    plaintext = input("Nexxus Secure AES ECB Encryption Service. Plaintext: ")
    plaintext = plaintext.rstrip("\n").rstrip("\r")
    result = encrypt(plaintext)
    print(result)

if __name__ == "__main__":
    main()
