import re
from sys import exit


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$",ip):
        print("True")
    else:
        exit("Nah")


if __name__ == "__main__":
    main()
