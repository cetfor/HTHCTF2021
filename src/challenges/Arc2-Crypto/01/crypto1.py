#!/usr/bin/env python3

import binascii
import random
from os import urandom

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

def xor_string(str1, str2):
    xor = bytes(a ^ b for a, b in zip(binascii.unhexlify(str1), binascii.unhexlify(str2)))
    return binascii.hexlify(xor).decode('utf-8')

FLAG = b"HTH{xor_has_interesting_properties}"
FLAG = binascii.hexlify(FLAG).decode('utf-8')
#print(f"FLAG = {FLAG}")

KEY1 = urandom(int(len(FLAG)/2))
KEY1 = binascii.hexlify(KEY1).decode('utf-8')
#print(f"KEY1 = {KEY1}")

KEY2 = urandom(int(len(FLAG)/2))
KEY2 = binascii.hexlify(KEY2).decode('utf-8')
#print(f"KEY2 = {KEY2}")

KEY3 = urandom(int(len(FLAG)/2))
KEY3 = binascii.hexlify(KEY3).decode('utf-8')
#print(f"KEY3 = {KEY3}")

messages = [
    "tell St0ke we're closing in on them quickly",
    "the fox hunt is on, triangulating safehouse location",
    "keep rotating the crypto keys",
]

print("[Hax4Headz RF SNIFFER v3.5.6] Intercepting messages...")
print(f"ZzZ~zzZ~ZZz~ {random.choice(messages)} ~ZzZ~zzZ~ZZz")
print("\n[Hax4Headz RF SNIFFER v3.5.6] Captured a raw message encoded with three unique keys...")
print(f"KEY1 = {KEY1}")
print(f"KEY2 ^ KEY1 = {xor_string(KEY2, KEY1)}")
print(f"KEY2 ^ KEY3 = {xor_string(KEY2, KEY3)}")
FLAG_KEY1 = xor_string(FLAG, KEY1)
KEY3_KEY2 = xor_string(KEY3, KEY2)
print(f"FLAG ^ KEY1 ^ KEY3 ^ KEY2 = {xor_string(FLAG_KEY1, KEY3_KEY2)}")
