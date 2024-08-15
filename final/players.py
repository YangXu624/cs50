class Player:
    def __init__(self, balance=100):
        self.balance = balance

    def action(self, current=2):
        act = input("Action: ").lower()

        if act == "check":
            print(f"Check")
            return self.balance
        elif "raise" in act:
            s = act.split(" ")
            amt = int(s[1])
            self.balance = self.balance - amt
            print(f"Raise by {amt}")
            return self.balance
        elif act == "call":
            self.balance = self.balance - current
            print(f"Call")
            return self.balance
        elif act == "fold":
            print(f"Fold")
            del self

player = Player()
player.action()
