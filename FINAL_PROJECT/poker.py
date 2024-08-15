from pokercards import Card
from random import choice

hand = tuple('', '')
hand[0] = choice(deck)
deck.remove(hand[0])
hand[1] = choice(deck)
deck.remove(hand[1])

print(hand)
