from sys import argv

def main():
    with open(f"{argv[2]}", "r") as file:
        rows = file.read()
        for row in enumerate(rows):
            print(row)

if __name__ == "__main()__":
    main()
