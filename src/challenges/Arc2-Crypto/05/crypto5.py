#!/usr/bin/env python3

import time
from Crypto.Util.number import long_to_bytes # pycryptodome
import hashlib

FLAG = b'HTH{speed_makes_it_possible}'

def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()

def encrypt(b):
    key = generate_key()
    if len(b) > len(key):
        return "Error: message too long!"
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()

def check_input(user_input):
    if not 'operation' in user_input:
        return {"error": "No operation found"}
    elif user_input['operation'] == 'encrypt_flag':
        return {"encrypted_flag": encrypt(FLAG)}
    elif user_input['operation'] == 'encrypt_data':
        data = bytes.fromhex(user_input['data'])
        return {"encrypted_data": encrypt(data)}
    else:
        return {"error": "Invalid operation"}

def main():
    print("Nexxus cryptographic service 2.0")
    while True:
        user_input = input()
        check_input(user_input)

if __name__ == "__main__":
    main()
