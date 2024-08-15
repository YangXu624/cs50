from cards import Card
from random import choice
from players import Player


#Argument river(list) and deck(list)
def round(river, deck):
    #Add one card to the river
    card = choice(deck)
    river.append(card)
    deck.remove(card)
    return river, deck


def bet(player, current):
    initial = player.balance
    #Perform action: Call/check/raise by n/fold
    player.balance = player.action(current)
    #If fold, add 0 to pot
    added_to_pot = initial - player.balance
    return added_to_pot


def main():
    #Inititate deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)

    #Initiate players
    players = []
    player1 = Player(name="Player 1")
    players.append(player1)

    #Initiate pot
    pot = 0

    #Give out hand to Player 1 (User)
    hand = ['Card 1', 'Card 2']
    for i in range(2):
        hand[i] = choice(deck)
        deck.remove(hand[i])
    print(f"\nYour hand is {hand}\n")

    #Pre-river betting
    #Current = Minimum bet
    current = 2
    #Each player takes turns to perform action
    for player in players:
        added = bet(player, current)
        print(f"{player.name} now has {player.balance}")
        pot += added
        print(f"Pot value: {pot}")

    #Iterate rounds
    river = []
    for i in range(5):
        print(f"Round {i + 1}")
        #Deal a card to the river
        river, deck = round(river, deck)
        print(f"River: {river}\n")

        #Current = Minimum bet
        current = 2
        #Each player takes turns to perform action
        for player in players:
            added = bet(player, current)
            print(f"{player.name} now has {player.balance}")
            pot += added
            print(f"Pot value: {pot}\n")


if __name__ == "__main__":
    main()
