from validator_collection import checkers

def main():
    inp = input("What's your email address? ")

    if checkers.is_email(inp):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
