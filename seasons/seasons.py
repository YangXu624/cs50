import datetime
import re
from sys import exit


def main():
    dt = input("Date of Birth: ")

    if dts := re.search(r"(\d{4})-(\d{2})-(\d{2})", dt):
        year, month, day = int(dts.group(1)), int(dts.group(2)), int(dts.group(3))
    else:
        sys.exit("Invalid input")

    print(datetime.datetime.today() - datetime.datetime(year, month, day))



...


if __name__ == "__main__":
    main()
