class Player:
    def __init__(self, balance=100):
        self.balance = balance

    def action():
        while True:
            try:
                act = input("Action: ").lower()
                
            except ValueError:
                print("Check/call/raise x/fold")
        if act == "check":
            print(f"Check. Balance = {self.balance}")

