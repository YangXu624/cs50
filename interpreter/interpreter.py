def main():
    math = input("Expression: ")

    w = operate(math)

    print()

def operate(eqn):
    x, y, z = eqn.split
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
