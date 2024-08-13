import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|10|11|12)(\:[0-5][0-9])? (AM|PM) to ([1-9]|10|11|12)(\:[0-5][0-9])? (AM|PM)$", s):
        first = [matches.group(1), matches.group(2), matches.group(3)]
        last = [matches.group(4), matches.group(5), matches.group(6)]

        if first[2] == "PM":
            if int(first[0]) < 12:
                first[0] = int(first[0]) + 12

        if last[2] == "PM":
            if int(last[0]) < 12:
                last[0] = int(last[0]) + 12

        if first[2] == "AM" and first[0] == "12":
            first[0] = 24
        if last[2] == "AM" and last[0] == "12":
            last[0] = 24

        if first[1] == None:
            first[1] = ":00"
        if last[1] == None:
            last[1] = ":00"

        if len(str(first[0])) == 1:
            first[0] = "0" + first[0]
        if len(str(last[0])) == 1:
            last[0] = "0" + last[0]

        if int(first[0]) == 24:
            first[0] = "00"
        if int(last[0]) == 24:
            last[0] = "00"

        return f"{first[0]}{first[1]} to {last[0]}{last[1]}"

    else:
        raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()
