import base64
import binascii
import codecs
import json
import telnetlib

HOST = "18.222.113.93"
PORT = 7809

def recv_prompt(tn):
    return tn.read_until(b"Nexxus Secure AES ECB Encryption Service. Plaintext: ", timeout=1)

def recv_ct(tn):
    return tn.read_until(b"}\n", timeout=1)

def send_line(tn, line):
    print(">> Sending: {}".format(line))
    tn.write(bytes(line, "utf8"))
    return recv_ct(tn)

def get_prompt(tn):
    received = recv_prompt(tn)
    print("\n>> Received - {}".format(received.decode("utf8").replace("\n", "")))

def get_reference_block(tn, string):
    tn = telnetlib.Telnet(HOST, PORT)
    get_prompt(tn)
    leaked_byte = send_line(tn, string)
    received = json.loads(leaked_byte.decode('utf8'))
    return received['ciphertext'][:32]

# A = input
# F = flag
# ? = padding
# G = guess

# AFFFFFFFFFFFFFF?
# AAFFFFFFFFFFFFFF????????????????
# AAAAAAAAAAAAAAAAFFFFFFFFFFFFFF??
# AAAAAAAAAAAAAAAFFFFFFFFFFFFFF??? <-- send this and record result!
# AAAAAAAAAAAAAAAGFFFFFFFFFFFFF??? <-- guess G until result matches recorded result!

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}{"

flag = ""
while len(flag) < 14:
    tn = telnetlib.Telnet(HOST, PORT)
    reference_block = get_reference_block(tn, "A"*(15-len(flag)) + "\n")
    for char in CHARSET:
        tn = telnetlib.Telnet(HOST, PORT)
        received = recv_prompt(tn)
        print("\n>> Received - {}".format(received.decode("utf8").replace("\n", "")))
        received = send_line(tn, "A"*(15-len(flag)) + flag + char + "\n")
        received = json.loads(received.decode('utf8'))
        if received['ciphertext'][:32] == reference_block:
            print(f"Match! -> {char}")
            flag += char
            break

print(flag)
