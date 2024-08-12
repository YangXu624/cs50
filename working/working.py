import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if = re.search(r"^(\d)(?:\:00)? (AM|PM) to (\d)(?:\:00)? (AM|PM)$", s):
        first = [matches.group(0), matches.group(2)]
        last = [matches.group(1), matches.group(3)]


...


if __name__ == "__main__":
    main()
