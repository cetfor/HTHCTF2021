import random
import sys

# Flag sequence: ~ b [1-9] w 0 B `
# Example sequence: ~ b 1 w 0 B `

# 1. Start the vehicle                      (~)   - state = 0 -> 1
# 2. Release the brake                      (b)   - state = 1 -> 2
# 3. Set the throttle limit to 1 or higher  (1-9) - state = 2 -> 3
# 4. Move forward                           (w)   - state = 3 -> 4
# 5. Set the throttle limit to 0 to stop    (0)   - state = 4 -> 5
# 6. Set the brake                          (B)   - state = 5 -> 6
# 7. Turn the engine off                    (`)   - if state == 6: show flag

VEHICLE_SPEED = 0
STATE_TRACKING = 0
VEHICLE_ON = False
WIPERS_ON = False
BRAKE_ON = True
BLINKERS_ON = False
RADIO_ON = False

OPS_BASE_MESSAGES = [
    "Have you done this before?",
    "Are you sure you know what you're doing?",
    "I don't know what to say anymore.",
    "What are you doing!? Keep it quiet!",
    "Are you trolling us?",
    "I just got a call from TSK, he says thanks for helping him out!",
    "Have you ever touched a computer before?",
    "Hey wake me up when you're done.",
]

# ops base 1 message
def ops_base_msg():
    # only print an ops message 33% of the time a "mistake" is made
    if random.choice([0, 0, 1]):
        print(f"*CRSHHH. This is ops base 1. {random.choice(OPS_BASE_MESSAGES)} Over*")

def set_throttle_limit_state():
    # User can freely change throttle limit between 1-9 without the state resetting.
    global STATE_TRACKING
    if STATE_TRACKING == 2:
        STATE_TRACKING += 1
    
# Number actions
def set_speed_0(): 
    global STATE_TRACKING
    global VEHICLE_SPEED
    if STATE_TRACKING == 4:
        STATE_TRACKING += 1
    else:
        STATE_TRACKING = 0
    if VEHICLE_ON and VEHICLE_SPEED >= 1:
        print(f"You set the throttle limit to 0. The vehicle stops.")
    else:
        print(f"You set the throttle limit to 0.")
    VEHICLE_SPEED = 0

def set_speed_1():
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 1.")
    VEHICLE_SPEED = 1

def set_speed_2():
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 2.")
    VEHICLE_SPEED = 2

def set_speed_3(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 3.")
    VEHICLE_SPEED = 3

def set_speed_4(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 4.")
    VEHICLE_SPEED = 4

def set_speed_5(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 5.")
    VEHICLE_SPEED = 5

def set_speed_6():
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 6.")
    VEHICLE_SPEED = 6

def set_speed_7(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 7.")
    VEHICLE_SPEED = 7

def set_speed_8(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    print(f"You set the throttle limit to 8.")
    VEHICLE_SPEED = 8

def set_speed_9(): 
    set_throttle_limit_state()
    global VEHICLE_SPEED
    VEHICLE_SPEED = 9
    print(f"You set the throttle limit to 9.")
    VEHICLE_SPEED = 9

# Malfunctions
def toggle_wipers():
    global WIPERS_ON
    if WIPERS_ON:
        WIPERS_ON = False
        print("*Windshield wipers turn off*")
    else:
        WIPERS_ON = True
        print("*Windshield wipers turn on*")
        ops_base_msg()

def toggle_blinkers():
    global BLINKERS_ON
    if BLINKERS_ON:
        BLINKERS_ON = False
        print("*Blinkers turn off*")
    else:
        BLINKERS_ON = True
        print("*Blinkers turn on*")
        ops_base_msg()

def toggle_radio():
    global RADIO_ON
    if RADIO_ON:
        RADIO_ON = False
        print("*The radio turns off*")
    else:
        RADIO_ON = True
        print("*The radio turns on*")
        print(f"*CRSHHH. This is ops base 1. I said keep it down this isn't time to blast Bieber! Over*")

# Q/q action
def jump_out():
    global VEHICLE_ON
    global VEHICLE_SPEED
    if VEHICLE_ON and VEHICLE_SPEED == 0:
        print("*You jump out of the vehicle while it's idling!*")
    elif VEHICLE_ON and VEHICLE_SPEED > 0:
        print("*You jump out of the vehicle while it's moving!*")
    else:
        print("*You jump out of the vehicle while it's off*")
    sys.exit()

# Start engine
def start_engine():
    global STATE_TRACKING
    global VEHICLE_ON
    global VEHICLE_SPEED
    if not VEHICLE_ON:
        VEHICLE_ON = True
        if VEHICLE_SPEED > 0:
            print("*You start the vehicle's engine. The vehicle's throttle limite resets to 0*")
            VEHICLE_SPEED = 0
        else:
            print("*You start the vehicle's engine*")
        if STATE_TRACKING == 0:
            STATE_TRACKING += 1
        elif STATE_TRACKING > 0:
            STATE_TRACKING = 0
    else:
        print("The vehicle is already running*")

# Toggle brake
def toggle_brake():
    global STATE_TRACKING
    global BRAKE_ON
    if BRAKE_ON:
        print("*You disable the parking brake*")
        BRAKE_ON = False
        if STATE_TRACKING == 1:
            STATE_TRACKING += 1
    else:
        print("*You enable the parking brake*")
        BRAKE_ON = True
        if STATE_TRACKING == 5:
            STATE_TRACKING += 1

# Stop engine
def stop_engine():
    global STATE_TRACKING
    global VEHICLE_ON
    if VEHICLE_ON:
        print("*You stop the vehicle's engine*")
        VEHICLE_ON = False
        if STATE_TRACKING == 6:
            show_flag()
        else:
            STATE_TRACKING = 0
    else:
        print("The vehicle is already off*")

def move_left():
    print("You cut the steering wheel left*")

def move_right():
    print("You cut the steering wheel right*")

def move_backward():
    if VEHICLE_ON:
        if VEHICLE_SPEED > 0:
            print("*The wheels smoke as the vehicle reverses at maximum speed*")
            print(f"*CRSHHH. This is ops base 1. This is CTF not GTA!!*")
    else:
        print(f"Nothing happens.")

def move_forward():
    global STATE_TRACKING
    if STATE_TRACKING == 3:
        STATE_TRACKING += 1
    if VEHICLE_ON:
        if VEHICLE_SPEED == 1:
            print(f"The vehicle lurches forward.")
        elif VEHICLE_SPEED == 2:
            print(f"The vehicle rolls forward.")
        elif VEHICLE_SPEED == 3:
            print(f"The vehicle moves forward.")
        elif VEHICLE_SPEED == 4:
            print(f"The vehicle speeds off!")
        elif VEHICLE_SPEED == 5:
            print(f"The vehicle speeds off!!")
        elif VEHICLE_SPEED == 6:
            print(f"The vehicle takes off quickly!")
        elif VEHICLE_SPEED == 7:
            print(f"The vehicle takes off like a bat out of hell!")
        elif VEHICLE_SPEED == 8:
            print(f"The vehicle's wheels squeal a bit before gaining traction and taking off!")
        elif VEHICLE_SPEED == 9:
            print(f"The vehicle burns out before taking off!")
        else:
            print(f"Nothing happens.")
    else:
        print(f"Nothing happens.")
    

def malfunction():
    malfunction = random.choice([1, 2, 3])
    if malfunction == 1:
        toggle_wipers()
    elif malfunction == 2:
        print("*Horn Honks*")
        ops_base_msg()
    elif malfunction == 3:
        toggle_blinkers()
    else:
        # This should never happen
        if VEHICLE_ON:
            print("*The vehicle backfires*")
        else:
            print("*The vehicle makes a strange noise*")

def show_flag():
    f = open("/home/re4/flag.txt", "r")
    flag = f.read()
    f.close()
    print(f"*CRSHHH. This is ops base 1. You did it! Accessing air duct... we found this: {flag}*")
    sys.exit()

def check_input(user_input):
    if user_input in input_to_function.keys():
        input_to_function[user_input]()
    else:
        malfunction()

input_to_function = {
    ###############################################################
    # numbers
    '0': set_speed_0,
    '1': set_speed_1,
    '2': set_speed_2,
    '3': set_speed_3,
    '4': set_speed_4,
    '5': set_speed_5,
    '6': set_speed_6,
    '7': set_speed_7,
    '8': set_speed_8,
    '9': set_speed_9,
    ###############################################################
    # upper characters
    "A": move_left,
    'B': toggle_brake,
    'D': move_right,
    'Q': jump_out,
    "S": move_backward,
    "W": move_forward,
    ###############################################################
    # lower characters
    "a": move_left,
    'b': toggle_brake,
    'd': move_right,
    'q': jump_out,
    "s": move_backward,
    "w": move_forward,
    ###############################################################
    # special characters
    "~": start_engine,
    "`": stop_engine,
    ###############################################################
    # special action strings
    "radio": toggle_radio,
}

def main():
    print("*CRSHHH. This is ops base 1. Remember to be very quiet! Over. CRSHHH*")
    print("*Interface uplink ready for input. You are now in control of the vehicle*")
    while True:
        user_input = input("$ >> ")
        check_input(user_input)


if __name__ == "__main__":
    main()