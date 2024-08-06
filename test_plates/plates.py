def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Check between 2 to 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    #Check no punctuation
    for i in range(len(s)):
        if s[i] == "." or s[i] == "!" or s[i] == " ":
            return False

    #Check first two characters are alphabets
    for i in range(2):
        if ord(s[i]) < 65 or ord(s[i]) > 90:
            return False

    for i in range(len(s) - 1):
        #If character i is an alphabet, ensure character i + 1 is not 0
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            if ord(s[i + 1]) == 48:
                return False
        #If character i is a number, ensure character i + 1 is not an alphabet
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            if ord(s[i + 1]) >= 65 and ord(s[i + 1]) <= 90:
                return False

    return True

if __name__ == "__main__":
    main()
