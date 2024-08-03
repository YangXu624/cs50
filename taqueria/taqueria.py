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
    item = get_str()
    price += float(taqueria[f"{item}"])
    print(f"${price}")

def get_str():
    str = input("Item:")

    return str
