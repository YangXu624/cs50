def main():
    fuel = convert()
    print(gauge(fuel))


def gauge(fuel):
    if fuel >= 99:
        return "F"
    elif fuel <= 1:
        return "E"
    else:
        return int(fuel)


def convert():
    while True:
        try:
            fuel = input("Fraction: ")
            numbers = fuel.split("/")
            x = int(numbers[0])
            y = int(numbers[1])
            percent = int(100 * round(float(x/y), 2))
        except ValueError:
            print("Not integer")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            if percent > 100:
                print("That's more than 100%")
            else:
                break

    return percent

main()
