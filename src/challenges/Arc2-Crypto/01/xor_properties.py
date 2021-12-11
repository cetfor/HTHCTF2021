import binascii

def xor_byte_string(str1, str2):
    return bytes(a ^ b for a, b in zip(str1, str2))

# Commutative: A ⊕ B = B ⊕ A
print(">> Checking Commutative property....", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("cafebabe")
try:
    assert xor_byte_string(A, B) == xor_byte_string(B, A)
    print("Commutative property holds!")
except AssertionError:
    print("Commutative property does not hold!")

# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
print(">> Checking Associative property....", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("cafebabe")
C = binascii.unhexlify("1337beef")
try:
    assert xor_byte_string(A, xor_byte_string(B, C)) ==  xor_byte_string(xor_byte_string(A, B), C)
    print("Associative property holds!")
except AssertionError:
    print("Associative property does not hold!")

# Identity: A ⊕ 0 = A
print(">> Checking Identity property.......", end=" ")
A = binascii.unhexlify("deadbeef")
B = binascii.unhexlify("00000000")
try:
    assert xor_byte_string(A, B) ==  A
    print("Identity property holds!")
except AssertionError:
    print("Identity property does not hold!")

# Self-Inverse: A ⊕ A = 0
print(">> Checking Self-Inverse property...", end=" ")
A = binascii.unhexlify("deadbeef")
try:
    assert xor_byte_string(A, A) == b'\x00\x00\x00\x00'
    print("Self-Inverse property holds!")
except AssertionError:
    print("Self-Inverse property does not hold!")
