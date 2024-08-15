class Player:
    def __init__(self, balance=100):
        self.balance = balance

    def action(self, current):
        act = input("Action: ").lower()

        if act == "check":
            print(f"Check. Balance = {self.balance}")
            return self.balance
        elif "raise" in act:
            s = act.split(" ")
            amt = int(s[1])
            

