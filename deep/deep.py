def main():
    qn = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    print(value(qn))

def value(x):
    match x:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"

main()
