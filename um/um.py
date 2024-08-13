import re
import sys


def main():
    print(count(input("Text: ")))


def count_substring(string, substring):
    return string.count(substring)


def count(s):
    substring = "hello"
    return s.count(substring)

...


if __name__ == "__main__":
    main()
