from sys import argv
import csv
from tabulate import tabulate


def main():
    prices = []

    file1 = get()
    with open(f"{file1}") as file:
        pizza = csv.DictReader(file)
        for row in pizza:
            prices.append(row)

    headers = []
    for item in prices[0].keys():
        headers.append(item)
    print(headers)

    print(tabulate(prices, headers = ", tablefmt = "grid"))


def get():
    try:
        if len(argv) > 2:
            exit("Too many command-line arguments")
        if len(argv) < 2:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "csv":
            exit("Not a CSV file")

        return argv[1]

    except FileNotFoundError:
        exit("File does not exist")
    except ValueError:
        exit("File does not exist")

if __name__ == "__main__":
    main()
