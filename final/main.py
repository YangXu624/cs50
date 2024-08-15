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


def bet(players):
    #Each player takes turns to perform action
    for player in players:
        #Perform action: Call/check/raise by n/fold
        player.action()


def main():
    #Inititate deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)

    #Initiate players
    players = []
    player1 = Player()
    players.append(player1)

    

    #Give out hand to Player 1 (User)
    hand = ['Card 1', 'Card 2']
    for i in range(2):
        hand[i] = choice(deck)
        deck.remove(hand[i])
    print(f"Your hand is {hand}\n")

    #Pre-river betting

    #Iterate rounds
    river = []
    for i in range(5):
        print(f"Round {i + 1}")
        #Deal a card to the river
        river, deck = round(river, deck)
        print(f"River: {river}\n")


if __name__ == "__main__":
    main()
