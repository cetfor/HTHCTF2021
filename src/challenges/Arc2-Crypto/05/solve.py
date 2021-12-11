import binascii
import telnetlib

from Crypto.Util import number

HOST = "18.222.113.93"
PORT = 7810

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    line = tn.read_until(b"\n", timeout=1)
    return line.decode()

def send(msg):
    if type(msg) == bytes:
        tn.write(msg)
    else:
        tn.write(bytes(msg, "utf8"))

def check_char(c, index):
    # =============================================
    # send flag request
    send("encrypted_flag\n")
    encrypted_flag = readline()
    #print(f"encrypted flag: {encrypted_flag}")
    a = encrypted_flag
    a = [a[i:i+2] for i in range(0,len(a)-1,2)]
    #print(a) # ['1f', 'a5', '7d', 'e0', '02', '9d', '68', '5a', '9e', '0c', '22', 'ed', '63', '48', 'e2', 'b5', '4c', '32', '62', 'e5', '8f', '78', 'aa', 'df', 'e2', 'bd', '1e', 'b4']

    # =============================================
    # send guess to be encrypted
    data = binascii.hexlify(flag.encode('utf8')).decode('utf8')
    send(data+"\n")
    encrypted_data = readline()
    #print(f"encrypted data: {encrypted_data}")
    b = encrypted_data
    b = [b[i:i+2] for i in range(0,len(b)-1,2)]
    #print(b)
    
    # =============================================
    if a[index] == b[index]:
        print(f"Match!: {c}")
        return True
    return False

flag = "????????????????????????????"
index = 0

# get welcome message
print(readline())

charset = "HTH}{abcdefghijklmnopqrstuvwxyz_1234567890"

#while index < len(flag):
while "?" in flag:    
    for char in charset:
        flag_list = list(flag)
        flag_list[index] = char
        flag = ''.join(flag_list)
        print(f"trying: {flag}")
        if check_char(char, index):
            print(flag)
            index += 1
            break
