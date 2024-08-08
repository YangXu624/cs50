from sys import argv, exit

from PIL import Image, ImageOps


def main():
    image1 = Image.open(f"{argv[1]}")
    image2 = Image.open("shirt.png")

    resized_shirt = ImageOps.fit(
    image2,
    (1200, 400),  # target size
    bleed=0.0,  # no bleeding
    centering=(0.0, 1.0)  # center the image
    )

    image1.paste(resized_shirt)
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
