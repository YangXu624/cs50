from cards import Card
from players import Player
from evaluate import ReturnStrongestHand

p1, p2 = Player(name="P1"), Player(name="P2")

#MANUALLY DEAL PLAYER1 HIS HAND
p1.hand = []
card21 = Card('3', 'spades')
card22 = Card('9', 'spades')
p1.hand.append(card21)
p1.hand.append(card22)

#MANUALLY DEAL BOT1 HIS HAND
p2.hand = []
card10 = Card('6', 'spades')
card20 = Card('7', 'spades')
p2.hand.append(card10)
p2.hand.append(card20)

#MANUALLY SET RIVER
river = []
card1 = Card('1', 'spades')
card2 = Card('2', 'spades')
card3 = Card('K', 'diamonds')
card4 = Card('4', 'clubs')
card5 = Card('5', 'spades')
river.append(card1)
river.append(card2)
river.append(card3)
river.append(card4)
river.append(card5)

allP1cards = river + p1.hand
allP2cards = river + p2.hand

def test_ReturnStrongestHand():
    assert ReturnStrongestHand(allP1cards, p1) == [2♠, 3♠, 4♠, 5♠, 6♠]
