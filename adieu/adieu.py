def main():
    list = []

    while True:
        try:
            list.append(input("Name: "))
        except EOFError:
            break

    print("Adieu, adieu, to", end = " ")

    for i in range(len(list) - 1):
        print(f"{list[i]}, ", end = "")

    print(f"and {list[len(list) - 1]}")

main()
