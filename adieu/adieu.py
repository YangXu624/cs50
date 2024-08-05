def main():
    list = []

    while True:
        try:
            list.append(input("Name: "))
        except EOFError:
            break

    print("Adieu, adieu, to", end = " ")

    if len(list) > 1:
        for i in range(len(list) - 1):
            print(f"{list[i]}, ", end = "")

        print(f"and {list[len(list) - 1]}")
    else:
        print(list[0])

main()
