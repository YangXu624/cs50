from pokercards import Card
from random import choice


def main():
    #Inititate deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)

    #Give out hand to Player 1 (User)
    hand = ['', '']
    hand[0] = choice(deck)
    deck.remove(hand[0])
    hand[1] = choice(deck)
    deck.remove(hand[1])

    #Pre-river betting
    #Deal river

if __name__ == "__main__":
    main()
