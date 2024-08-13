def main():
    print(count(input("Text: ")))


def count_substring(string, substring):
    return string.count(substring)


def count(s):
    substring = " um"
    c = s.count(substring)

    string = (f"{s[0]}{s[1]})").lower()

    print(string)

    if string == "um":
        c += 1

    return c


if __name__ == "__main__":
    main()
