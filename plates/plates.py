def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    for i in range(len(s)):
        if ord(s[i]) < 65 or ord(s[i]) > 90:
            return False


main()
