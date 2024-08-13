import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if " um" in s:
        return 1


...


if __name__ == "__main__":
    main()
