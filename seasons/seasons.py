import datetime
import re
from sys import exit
from num2words import num2words


def main():
    print(f"{check(input("Date of Birth: "))} minutes")

def check(dt):
    if dts := re.search(r"(\d{4})-(\d{2})-(\d{2})", dt):
        year, month, day = int(dts.group(1)), int(dts.group(2)), int(dts.group(3))
    else:
        sys.exit("Invalid input")

    list1 = str(datetime.datetime.today() - datetime.datetime(year, month, day))
    list2 = list1.split(" ")
    days = int(list2[0])

    return num2words((days - 1) * 24 * 60).replace(" and", "").capitalize()

...


if __name__ == "__main__":
    main()
