import random


def main():
    ...


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0 and lvl < 4:
                return lvl
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return 


if __name__ == "__main__":
    main()
