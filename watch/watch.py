import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    list = s.split(" ")

    for item in list:
        if re.search(r"^[s][r][c].+$"):
            src = item

    return item




if __name__ == "__main__":
    main()
