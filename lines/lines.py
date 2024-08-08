from sys import argv, exit

def main():
    file_name = get()
    print(count(file_name))


def get():
    try:
        if len(argv) > 2:
            exit("Too many command-line arguments")
        if len(argv) < 2:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "py":
            exit("Not a Python file")

        return argv[1]

    except FileNotFoundError:
        exit("File does not exist")
    except ValueError:
        exit("File does not exist")


def count(file_name):
    with open(f"{file_name}", "r") as file:
            rows = file.readlines()
            count = 0
            for i in range(len(rows)):
                line = rows[i].strip()
                if line == "":
                    continue
                elif line[0] == "#":
                    continue
                else:
                    count += 1
    return count


if __name__ == "__main__":
    main()
