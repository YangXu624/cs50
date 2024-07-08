def main():
    math = input("Expression: ")

    w = operate(math)

    print("{:.1f}".format(w))

def operate(eqn):
    x, y, z = eqn.split()
    x = float(x)
    z = float(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

main()
