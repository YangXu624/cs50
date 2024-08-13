import re
import validators

def main():
    inp = input("What's your email address? ")

    # Regular expression to match a valid email address
    regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

    if re.search(regex, inp):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
