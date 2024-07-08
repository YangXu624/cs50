def main():
    line = input()

    print(convert(line))

def convert(st):
    return st.replace(":)", "🙂").replace(":(", "🙁")

main()
