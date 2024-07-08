def main():
    t = convert(input("What time is it? "))

    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")

def convert(time):
    h, min = float(time.split(":"))
    value = h + (min / 60)
    return value


if __name__ == "__main__":
    main()
