def main():
    m = int(input("m = "))

    print(joule(m))

def joule(x):
    e = x * (300000000 ** 2)
    return e

main()
