from sys import argv, exit

from PIL import Image, ImageOps


def main():
    get()

    image1 = Image.open(f"{argv[1]}")
    image1 = ImageOps.fit(
    image1,
    size=image1.size,
    bleed=0.0,  # no bleeding
    centering=(0.5, 0.5)  # center the image
    )

    shirt = Image.open("shirt.png")
    size = shirt.size
    resized_shirt = ImageOps.fit(
    shirt,
    size,  # target size
    bleed=0.0,  # no bleeding
    centering=(0.0, 1.0)  # center the image
    )

    image1.paste(resized_shirt, (0, 400), resized_shirt)
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
