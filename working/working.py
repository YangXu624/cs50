import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|10|11|12)\:([0-5][0-9])? (AM|PM) to ([1-9]|10|11|12)\:([0-5][0-9])? (AM|PM)$", s):
        first = [matches.group(1), matches.group(2), matches.group(3)]
        last = [matches.group(4), matches.group(5), matches.group(6)]

    else:
        return

    if first[2] == "AM":
        return (first, last)
    elif first[2] == "PM":
        return ()

...


if __name__ == "__main__":
    main()
