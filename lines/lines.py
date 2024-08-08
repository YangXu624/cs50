from sys import argv, exit, argc
import os

def main():
    try:
        if argc > 2:
            exit("Too many command-line arguments")
        if argc < 2:
            exit("Too few command-line arguments")

        if not arg[1].endswith('.py'):
            exit("The provided file is not a Python file.")

        with open(f"{argv[1]}", "r") as file:
            rows = file.readlines()
            count = 0
            for i in range(len(rows)):
                count += 1
        print(count)
    except FileNotFoundError:
        exit("File does not exist")

if __name__ == "__main__":
    main()
