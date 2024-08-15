class Player:
    def __init__(self, name, balance=100, fold=False):
        self.name = name
        self.balance = balance
        self.fold = fold

    def action(self, current):
        #Only continue if player has not folded
        if self.fold == False:
            act = input("Action: ").lower()

            #Only allow 'check' if current = 0
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

            #If player folds, set fold=True
            elif act == "fold":
                self.fold = True
                print(f"Fold")
                return self.balance
        else:
            print(f"{self.name} has folded")
            return self.balance
