#Current bot operates on randomness, zero strategy
from random import randint


class Bot:
    def __init__(self, name, hand=['Card 1', 'Card 2'], current_bet=0, balance=100, fold=False):
        self.name = name
        self.hand = hand
        #Within a specific round, keeps track of how much the player has already betted
        self.current_bet = current_bet
        self.balance = balance
        self.fold = fold

    def action(self, current):
        #Only continue if bot has not folded
        if self.fold == False:
            diff = current - self.current_bet
            #Generate a number, to determine probability
            number = randint(1, 100)

            if current == 0:
                if number < 51:
                    print(f"{self.name} checks!")
                    return self.balance
                else:
                    amt = current + 10
                    self.balance = self.balance - amt
                    print(f"{self.name} raises by 10!")
                    return self.balance

            if number > 0 and number < 31:
                amt = diff + 10
                self.balance = self.balance - amt
                print(f"{self.name} raises by 10!")
                return self.balance

            elif number > 30 and number < 91:
                self.balance = self.balance - diff
                print(f"{self.name} calls!")
                return self.balance

            #If player folds, set fold=True
            else:
                self.fold = True
                print(f"{self.name} folds!")
                return self.balance

        else:
            print(f"{self.name} has folded")
            return self.balance
