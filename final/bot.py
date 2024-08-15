#Current bot operates on randomness, zero strategy
from random import randint


class Bot:
    def __init__(self, name, hand=['Card 1', 'Card 2'], balance=100, fold=False):
        self.name = name
        self.hand = hand
        self.balance = balance
        self.fold = fold

    def action(self, current=2):
        #Only continue if bot has not folded
        if self.fold == False:
            #Generate a number, to determine probability
            number = randint(1, 100)

            if current == 0 and number < 51:
                print(f"{self.name} checks!")
                return self.balance

            if number > 0 and number < 31:
                amt = current + 10
                self.balance = self.balance - amt
                print(f"{self.name} raises by 10!")
                return self.balance

            elif number > 30 and number < 91:
                self.balance = self.balance - current
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
