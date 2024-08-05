import random

def main():
    ans = int(get_int())

    while True:
        num = int(input("Guess: "))
        if compare(ans, num):
            return

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

def compare(ans, gs):
    if ans > gs:
        print("Too small!")
    elif ans < gs:
        print("Too large!")
    elif ans == gs:
        print("Just right!")
        return True
    else:
        print("How even")

main()
