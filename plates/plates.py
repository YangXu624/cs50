def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    for i in range(2):
        if ord(s[i]) < 65 or ord(s[i]) > 90:
            return False

    #Starting from the 3rd character, if character i is an alphabet, ensure character i + 1 is not 0
    for i in range(len(s) - 2):
        if ord(s[i + 2]) >= 65 and ord(s[i + 2]) <= 90:
            if s[i + 3] == 0:
                return False

main()
