import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d)(?:\:00)? AM|PM to (\d)(?:\:00)? AM|PM$", s)
        print(matches)




...


if __name__ == "__main__":
    main()
