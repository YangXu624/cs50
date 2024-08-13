from datetime import date
import re
from sys import exit
import inflect

p = inflect.engine()


def main():
    print(f"{check(input("Date of Birth: "))} minutes")

def check(dt):
    if dts := re.search(r"(\d{4})-(\d{2})-(\d{2})", dt):
        year, month, day = int(dts.group(1)), int(dts.group(2)), int(dts.group(3))
    else:
        exit("Invalid input")

    today = date.today()
    diff = (today - date(year, month, day)).days

    return p.number_to_words((diff) * 24 * 60).replace(" and", "").capitalize()


if __name__ == "__main__":
    main()
