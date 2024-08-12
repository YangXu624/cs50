import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|10|11|12)\:([0-5][0-9])? (AM|PM) to ([1-9]|10|11|12)\:([0-5][0-9])? (AM|PM)$", s):
        first = [matches.group(1), matches.group(2), matches.group(3)]
        last = [matches.group(4), matches.group(5), matches.group(6)]
        print(first, last)
    else:
        return


...


if __name__ == "__main__":
    main()
