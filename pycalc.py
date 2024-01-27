
n = int(input("n: "))
h = int(input("h: "))
x = int(input("x: "))
y = int(input("y: "))

def f(x, y):
    return (x - x * y)

for i in range(n):
    print(f(x, y))

    y += h * f(x, y)
    print(y)

    x += h
    print(x)
