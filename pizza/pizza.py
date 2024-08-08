from sys import argv
import csv


def main():
    pztype = get()


def get():
    try:
        if len(argv) > 2:
            exit("Too many command-line arguments")
        if len(argv) < 2:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "csv":
            exit("Not a CSV file")

        return argv[1]

    except FileNotFoundError:
        exit("File does not exist")
    except ValueError:
        exit("File does not exist")

if __name__ == "__main__":
    main()
