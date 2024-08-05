import random

def main():
    number = get_int()
    print(number)

def get_int():
    while True:
        try:
            lvl = input("Level: ")
            num = random.randint(1, int(lvl))
            return num
        except ValueError:
            continue
        except EOFError:
            break

main()
