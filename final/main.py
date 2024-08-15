from pokercards import Card
from random import choice

def round(river, deck):
    #Add one card to the river
    river.append(choice(deck))
    return river


def main():
    #Inititate deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)

    #Give out hand to Player 1 (User)
    hand = ['Card 1', 'Card 2']
    for i in range(2):
        hand[i] = choice(deck)
        deck.remove(hand[i])
    print(hand)

    #Pre-river betting
    #Iterate rounds
    river = []
    


if __name__ == "__main__":
    main()
