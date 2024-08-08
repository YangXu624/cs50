from sys import argv

def main():
    with open(f"{argv[1]}", "r") as file:
        for row in enumerate(file):
            print(row)

if __name__ == "__main()__":
    main()
