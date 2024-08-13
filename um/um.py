def main():
    print(count(input("Text: ")))


def count_substring(string, substring):
    return string.count(substring)


def count(s):
    substring1 = " um"
    substring2 = "Um"
    return s.count(substring1) + s.count(substring2)


if __name__ == "__main__":
    main()
