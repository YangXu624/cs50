from sys import argv


def main():
    get()


def get():
    try:
        if len(argv) > 3:
            exit("Too many command-line arguments")
        if len(argv) < 3:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "csv":
            exit("Not a CSV file")

        three, four = argv[2].split(".")
        if four != "csv":
            exit("Not a CSV file")

        return argv[1], argv[2]

    except FileNotFoundError:
        exit("File does not exist")
    except ValueError:
        exit("File does not exist")


if __name__ == "__main__":
    main()

