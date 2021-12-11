#!/usr/bin/env python3

import base64
import codecs
import json
import random

"""
Credit: https://cryptohack.org/challenges/general/ "Encoding Challenge"
"""

CHALLENGES_TILL_FLAG = 100
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "utf-8",
]
WORDS = []

#def read_flag(flag_file="flag.txt"):
def read_flag(flag_file="/home/crypto2/flag.txt"):
    f = open(flag_file, "r")
    flag = f.read()
    f.close()
    return flag

class Challenge():
    def __init__(self):
        self.challenge_words = ""
        self.stage = 0
        self.active = True

    def create_level(self):
        self.stage += 1
        self.challenge_words = "_".join(random.choices(WORDS, k=3))
        encoding = random.choice(ENCODINGS)

        if self.stage == CHALLENGES_TILL_FLAG - 1:
            self.active = False
            #return json.dumps({"flag": read_flag()})
            #return json.dumps({"flag": "HTH{data_encoding_is_very_important}"})
            return "HTH{data_encoding_is_very_important}"
        
        if encoding == "base64":
            encoded = base64.b64encode(self.challenge_words.encode()).decode()
        elif encoding == "hex":
            encoded = self.challenge_words.encode().hex()
        elif encoding == "rot13":
            encoded = codecs.encode(self.challenge_words, 'rot_13')
        elif encoding == "utf-8":
            encoded = [ord(b) for b in self.challenge_words]
        return json.dumps({"type": encoding, "encoded": encoded})

    def challenge(self, user_input):
        if self.stage == 0:
            return self.create_level()
        elif self.challenge_words == user_input:
            return self.create_level()
        raise TypeError


def main():
    #with open('rockyou.txt', 'r', encoding="utf8") as f:
    with open('/home/crypto2/rockyou.txt', 'r', encoding="utf8") as f:
        for line in f.readlines():
            try:
                WORDS.append(line.strip().replace("'", ""))
            except UnicodeDecodeError as e:
                pass
    
    # Create challenge
    chal = Challenge()
    level = chal.challenge("")

    while True:
        print(f"Level {chal.stage}: {level}")
        user_input = ""
        try:
            user_input = input("Response: ")
        except EOFError as e:
            pass
        
        try:
            level = chal.challenge(user_input)
        except TypeError as e:
            print(f"Level {chal.stage} of {CHALLENGES_TILL_FLAG} failed. Hanging up.")
            return
        
        if not chal.active:
            break
        
if __name__ == "__main__":
    main()
