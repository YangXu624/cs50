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
    link = src[1].replace("/embed", "").replace("youtube.com", "youtu.be").replace("www.", "")

    test = link.split("/")
    if "youtu.be" not in test[2]:
        print(test)
        return None

    if "https" in link:
        return link
    else:
        return link.replace("http", "https")


if __name__ == "__main__":
    main()
