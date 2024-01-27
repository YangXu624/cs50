import math

n = int(input("n: "))
h = float(input("h: "))
x = float(input("x: "))
y = float(input("y: "))

def f(x, y):
    return (x + y - 1)

for i in range(n):

    k1 = h * f(x, y)
    k2 = h * f((x + h), (y + k1))

    print(f"n = {i}, x = {x}, y = {y}, k1 = {k1}, k2 = {k2}")

    y += (k1 + k2) / 2
    x += h



