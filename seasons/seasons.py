from datetime import date
import re


def main():
    while True:
        dt = input("Date of Birth: ")

        if dts := re.search(r"(\d{4})-(\d{2})-(\d{2})", dt):
            year, month, day = dts.group(1), dts.group(2), dts.group(3)

        print(year, month, day)


...


if __name__ == "__main__":
    main()
