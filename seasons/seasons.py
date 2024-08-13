from datetime import date
import re
from sys import exit


def main():
    dt = input("Date of Birth: ")

    if dts := re.search(r"(\d{4})-(\d{2})-(\d{2})", dt):
        year, month, day = dts.group(1), dts.group(2), dts.group(3)
    else:
        sys.exit("Invalid input")

    


...


if __name__ == "__main__":
    main()
