import argparse

def main(challenge):
    shift = ord(challenge[0])
    abc = "abcdefghijklmnopqrstuvwxyz"
    response = "".join([abc[(abc.find(c) + shift) % 26] for c in challenge])
    print(f"Response should be: {response}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTHCTF2021 RE02 Solve Script")
    parser.add_argument("challenge", help="challenge string")
    args = parser.parse_args()
    main(args.challenge)
