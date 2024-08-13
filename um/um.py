import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    substring = "hello"

    count = count_substring(s, substring)
    return count


...


if __name__ == "__main__":
    main()
