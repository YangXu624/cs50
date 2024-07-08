def main():
    name = input("camelCase: ")

    print("snake_case:", convert(name))

def convert(st):
    for i in range(len(st)):
        if st[i].isupper():
            st[i].append("_")
    return st

main()
