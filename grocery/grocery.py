def main():
    gcr = get_arg()

    unique = {}
    for i in range(len(gcr)):
        gcr[i] = gcr[i].upper()

        if gcr[i] in unique:
            unique[f"{gcr[i]}"] += 1
        else:
            unique[f"{gcr[i]}"] = 1

    print(unique)

def get_arg():
    groceries = []
    while True:
        try:
            arg = input()
            groceries.append(arg)
        except EOFError:
            return groceries

main()
