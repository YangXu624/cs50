import re
import sys
import string


def main():
    print(count(input("Text: ")))


def count_substring(string, substring):
    return string.count(substring)


def count(s):
    substring = "hello"

    count = count_substring(s, substring)
    return count


...


if __name__ == "__main__":
    main()
