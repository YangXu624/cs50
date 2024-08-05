import random


def main():
    score = 0
    lvl = get_level()
    for i in range(10):
        pair = generate_integer(lvl)
        sol = int(pair[0]) + int(pair[1])

        count = 0

        while count < 3:
            try:
                ans = int(input(f"{pair[0]} + {pair[1]} = "))

                if ans == sol:
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1

                if count == 3:
                    print(f"{pair[0]} + {pair[1]} = {sol}")
            except ValueError:
                continue

    print("Score:", score)

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
        pair = [random.randint(0, 9), random.randint(0, 9)]
    elif level == 2:
        pair = [random.randint(10, 99), random.randint(10, 99)]
    else:
        pair = [random.randint(100, 999), random.randint(100, 999)]
    return pair


if __name__ == "__main__":
    main()
