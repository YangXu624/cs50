import math

n = int(input("n: "))
h = float(input("h: "))
x = float(input("x: "))
y = float(input("y: "))

def f(x, y):
    return (x + y - 1)

for i in range(n):
    print(f"n = {i}, x = {x}, y = {y}, f(x, y) = {f(x, y)}")

    k1 = h * f(x, y)
    k2 = h * f((x + h), (y + k1))

    y += h * (k1 + k2) / 2
    x += h



