def main():
    gcr = get_arg()

    for i in range(len(gcr)):
        gcr[i] = gcr[i].toupper()

    print(gcr)

def get_arg():
    groceries = []
    while True:
        try:
            arg = input()
            groceries.append(arg)
        except EOFError:
            return groceries

main()
