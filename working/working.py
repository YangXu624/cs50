import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|10|11|12)(?:\:00)? (AM|PM) to ([1-9]|10|11|12)(?:\:00)? (AM|PM)$", s):
        first = [matches.group(1), matches.group(2)]
        last = [matches.group(3), matches.group(4)]
        print(first, last)
    else:
        return


...


if __name__ == "__main__":
    main()
