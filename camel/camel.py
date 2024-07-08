def main():
    name = input("camelCase: ")

    print("snake_case:", convert(name))

def convert(st):
    for i in range(len(st)):
        if st[i].isupper():
            st = st.replace(st[i], "_" + st[i].lower())

    return st

main()
