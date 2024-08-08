from sys import argv, exit

from PIL import Image


def main():
    images = []

    for arg in argv[1:]:
        img = Image.open(arg)
        images.append(img)

    images[0].paste(images[1])
    images[0].save(f"{argv[2]}")

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
