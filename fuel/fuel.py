def main():
    while True:
        try:
            fuel = input("Fraction: ")
            numbers = fuel.split("/")
            x = int(numbers[0])
            y = int(numbers[1])
            percent = 100 * round(float(x/y), 2)

        except ValueError:
            print("Not integer")

        except ZeroDivisionError:
            print("Cannot divide by zero")

        else:
            print("HI")
            break

    print(percent, "%")

main()
