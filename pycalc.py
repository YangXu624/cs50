
n = int(input("n: "))
h = float(input("h: "))
x = float(input("x: "))
y = float(input("y: "))

def f(x, y):
    return (x - x * y)

for i in range(n):
    print(1, f(x, y), end="")

    y += h * f(x, y)
    print(y, end="")

    x += h
    print(x)
