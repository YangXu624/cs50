def main():
    fuel = input("Fraction: ")
    numbers = fuel.split("/")
    try:
        x = int(numbers[0])
        y = int(numbers[1])
    except ValueError:

    print(convert(fuel))

def convert(x):
    numbers = x.split("/")
    percent = float(numbers[0])/float(numbers[1])
    return percent

main()
