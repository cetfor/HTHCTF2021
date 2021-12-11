#!/usr/bin/env python3

import time

def main():
    flag = "HTH{time_can_tell_us_a_lot}"
    
    while True:
        user_input = input("Enter code >> ")
        if len(user_input) < len(flag):
            print("Too short, St0ke.")
            return
        elif len(user_input) > len(flag):
            print("Too long, St0ke.")
            return
        else:
            print("Standby, St0ke. Checking code...")
            for i, _ in enumerate(user_input):
                if user_input[i] == flag[i]:
                    time.sleep(0.5)
            
            if user_input == flag:
                print("Welcome, St0ke. Sending beacon locations...")
                print("*You squint your eyes as your terminal illuminates - hundreds") 
                print("of lines of GPS corrdinates and identifiers fill the screen.*")
                print("B3nny steps next to you in awe. \"You found them\"")
                return
            else:
                print("Incorrect.")
                return

if __name__ == "__main__":
    main()
