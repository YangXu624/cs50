import random
from sys import exit

def main():
    try:
        ans = int(get_int())
    except TypeError:
        return

    while True:
        try:
            num = int(input("Guess: "))
            if compare(ans, num):
                exit("Just right!")
        except ValueError:
            continue

def get_int():
    while True:
        try:
            lvl = input("Level: ")
            num = random.randint(1, int(lvl))
            return num
        except ValueError:
            continue
        except EOFError:
            print("")
            break

def compare(ans, gs):
    if ans > gs:
        print("Too small!")
        return False
    elif ans < gs:
        print("Too large!")
        return False
    elif ans == gs:
        return True

main()
