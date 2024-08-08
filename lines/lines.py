from sys import argv

def main():
    with open(f"{argv[1]}", "r") as file:
        rows = file.readlines()
        count = 0
        for i in range(len(rows)):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
