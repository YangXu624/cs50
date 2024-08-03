def main():
    while True:
        fuel = input("Fraction: ")
        numbers = fuel.split("/")

        for i in range(len(fuel)):
            if fuel[i] == "/":
                break

    print(convert(fuel))

def convert(x):
    numbers = x.split("/")
    percent = float(numbers[0])/float(numbers[1])
    return percent

main()
