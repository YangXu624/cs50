

h = int(input("h: "))
x = int(input("x: "))
y = int(input("y: "))

def f(x, y):
    return (x - x * y)


y += h * f(x, y)
x += h
