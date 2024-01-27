import math

n = int(input("n: "))
h = float(input("h: "))
x = float(input("x: "))
y = float(input("y: "))

def f(x, y):
    return ((y) / (x))

for i in range(n):
    print(f"n = {i}, x = {x}, y = {y}, f(x, y) = {f(x, y)}")

    y += h * f(x, y)
    x += h



