import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    list = s.split(" ")

    for item in list:
        if re.search(r"^[s][r][c].+$", item):
            src = item

    src = src.split('"')
    link = src[1].replace("/embed", "")

    return link


if __name__ == "__main__":
    main()
