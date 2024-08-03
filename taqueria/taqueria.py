taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price = float(0)
    while True:
        item = get_str()
        if item == "":
            break
        price += round(float(taqueria[f"{item}"]), 2)
        print("$", "%.2f" % price, sep = "")

def get_str():
    while True:
        try:
            str = input("Item: ")
            if str == "":
                return str
            price = taqueria[f"{str}"]
        except KeyError:
            print("Not in menu")
        else:
            return str

main()
