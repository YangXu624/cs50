from sys import argv, exit

from PIL import Image


def main():
    image1 = Image.open(f"{argv[1]}")
    image2 = Image.open("shirt.png")

    PIL.ImageOps.fit(image2, tuple[1, 1], int = Resampling.BICUBIC, float = 0.0, tuple[0.5, 0.5])

    image1.paste(image2)
    image1.save(f"{argv[2]}")


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
