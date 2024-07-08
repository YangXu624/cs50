def main():
    bal = 50
    while True:
        if bal > 0:
            print("Amount Due:", bal)
            amt = insert()
            bal = int(bal) - amt
        else:
            bal = (-1) * int(bal)
            print("Change Owed:", bal)
            break

def insert():
    amt = int(input("Insert Coin: "))
    if amt == 5 or amt == 10 or amt == 25:
        return amt
    else:
        return 0

main()
