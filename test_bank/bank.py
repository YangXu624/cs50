def main():
    greet = input("Greeting: ").lower().strip().split()
    print(check(greet[0]))

def check(x):
    if x == "hello" or x == "hello!" or x == "hello,":
        return "$0"
    elif x[0] == "h":
        return "$20"
    else:
        return "$100"

main()
