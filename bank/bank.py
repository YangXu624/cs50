def main():
    greet = input("Greeting: ").lower().strip().split()
    print(f"${value(greet[0])}")

def value(x):
    if x == "hello" or x == "hello!" or x == "hello,":
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
