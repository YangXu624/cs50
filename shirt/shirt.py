from sys import argv, exit
from PIL import Image


def main():



def get():
    try:
        if len(argv) > 3:
            exit("Too many command-line arguments")
        if len(argv) < 3:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "png" and two != "jpg" and two != "jpeg":
            exit("Not a compatible file")

        three, four = argv[2].split(".")
        if four != two:
            exit("Output file does not match input")

        return argv[1], argv[2]

    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")
    except ValueError:
        exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()
