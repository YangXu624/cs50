from sys import argv, exit

from PIL import Image, ImageOps


def main():
    get()

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(argv[1])

    except FileNotFoundError:
        exit("Could not find the image file")

    else:
        size = shirt.size
        before = ImageOps.fit(before, size)
        before.paste(shirt, box = (0, 0), mask = shirt)
        before.save(argv[2], format=None)


def get():
    try:
        if len(argv) > 3:
            exit("Too many command-line arguments")
        if len(argv) < 3:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "png" and two != "jpg" and two != "jpeg":
            exit("Invalid input")

        three, four = argv[2].split(".")
        if four != two:
            exit("Input and output have different extensions")

        return argv[1], argv[2]

    except FileNotFoundError:
        exit("Invalid input")
    except ValueError:
        exit("Invalid input")


if __name__ == "__main__":
    main()
