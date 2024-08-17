class Player:
    def __init__(self, name, hand=['Card 1', 'Card 2'], current_bet=0, balance=100, fold=False):
        self.name = name
        self.hand = hand
        #Within a specific round, keeps track of how much the player has already betted
        self.current_bet = current_bet
        self.balance = balance
        self.fold = fold

    def action(self, current):
        diff = current - self.current_bet
        #Only continue if player has not folded
        if self.fold == False:
            while True:
                try:
                    act = input("Action: ").lower()

                    #Only allow 'check' if current = 0
                    if act == "check":
                        if diff == 0:
                            print(f"{self.name} checks!")
                            return self.balance
                        else:
                            print("Cannot check!")

                    elif "raise" in act:
                        s = act.split(" ")
                        amt = diff + int(s[1])
                        self.balance = self.balance - amt
                        print(f"{self.name} raises by {s[1]}!")
                        return self.balance

                    elif act == "call":
                        if diff == 0:
                            raise ValueError("Can't call when there is no bet. Did you mean 'call'?")
                        else:
                            self.balance = self.balance - diff
                            print(f"{self.name} calls!")
                            return self.balance

                    #If player folds, set fold=True
                    elif act == "fold":
                        self.fold = True
                        print(f"{self.name} folds!")
                        return self.balance
                except ValueError:
                    print("")
                    continue

        else:
            print(f"{self.name} has folded")
            return self.balance
