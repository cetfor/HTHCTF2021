import binascii

# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

def xor_string(str1, str2):
    xor = bytes(a ^ b for a, b in zip(binascii.unhexlify(str1), binascii.unhexlify(str2)))
    return binascii.hexlify(xor).decode('utf-8')

#KEY1 = 4d15dba1b41f02f1c5940770d68a5caab69fafe213b1b9d7d0b363f650baceb6733910
#KEY2 ^ KEY1 = a1781de001d739818157f3d4c7d9e13b457814a1c90cf13b5cdb12706a0fd469046c1b
#KEY2 ^ KEY3 = 4af469eae4555af487b8080f1374a180fd9002541d5d2f46be86778f953c9c270715c9
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 4fb5fa3028252a5a2a4d7c20ac90894f396adec26782f1ce1e477b09a0f426f8115fa4

# Imput your values here:
KEY1 = "4d15dba1b41f02f1c5940770d68a5caab69fafe213b1b9d7d0b363f650baceb6733910"
KEY2_KEY1 = "a1781de001d739818157f3d4c7d9e13b457814a1c90cf13b5cdb12706a0fd469046c1b"
KEY2_KEY3 = "4af469eae4555af487b8080f1374a180fd9002541d5d2f46be86778f953c9c270715c9"
FLAG_KEY1_KEY3_KEY2 = "4fb5fa3028252a5a2a4d7c20ac90894f396adec26782f1ce1e477b09a0f426f8115fa4"

key1 = KEY1
key2 = xor_string(KEY2_KEY1, key1)
key3 = xor_string(key2, KEY2_KEY3)

a = xor_string(key1, FLAG_KEY1_KEY3_KEY2)
b = xor_string(a, key2)
c = xor_string(b, key3)
flag = c

print(f"Key1: {key1}")
print(f"Key2: {key2}")
print(f"Key3: {key3}")
print(f"Flag: {binascii.unhexlify(flag).decode('utf-8')}")
