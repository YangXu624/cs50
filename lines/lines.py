from sys import argv, exit

def main():
    try:
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
