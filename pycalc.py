
n = int(input("n: "))
h = float(input("h: "))
x = float(input("x: "))
y = float(input("y: "))

def f(x, y):
    return (x - x * y)

for i in range(n):
    print(f"n = {i}", end="")

    print(f"y = {y}", end="")
    y += h * f(x, y)

    print(f"x = {x}", end="")
    x += h

    print(f(x, y), end="")


