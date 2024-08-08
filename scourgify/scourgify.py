from sys import argv, exit
import csv


def main():
    temp = []
    list_dict = []

    try:
        file1, file2 = get()
        with open(f"{file1}") as f1:
            x = csv.DictReader(f1)

            for row in x:
                temp.append(row)

            for dict in temp:
                last, first = dict["name"].split(", ")
                list_dict.append({"first": first, "last": last, "house": dict["house"]})

        with open(f"{file2}", "w") as f2:
            y = csv.DictWriter(f2, fieldnames = ["first", "last", "house"])
            y.writerow(list_dict)

    except FileNotFoundError:
        exit(f"Could not read {file1}")




def get():
    try:
        if len(argv) > 3:
            exit("Too many command-line arguments")
        if len(argv) < 3:
            exit("Too few command-line arguments")

        one, two = argv[1].split(".")
        if two != "csv":
            exit("Not a CSV file")

        three, four = argv[2].split(".")
        if four != "csv":
            exit("Not a CSV file")

        return argv[1], argv[2]

    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")
    except ValueError:
        exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()
