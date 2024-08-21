import pytest
from cards import Card
from players import Player
from evaluate import ReturnStrongestHand, ReturnWinner, ReturnFlush, ReturnStraight, ReturnPair, ReturnTriple, ReturnFourOfAKind, ReturnFullHouse, StrongestSingleCard

@pytest.fixture
def setup_players_and_river():
    p1 = Player(name="P1")
    p2 = Player(name="P2")

    # Deal Player 1 their hand
    p1.hand = [Card('3', 'spades'), Card('9', 'spades')]

    # Deal Player 2 their hand
    p2.hand = [Card('6', 'spades'), Card('7', 'spades')]

    # Set River
    river = [
        Card('2', 'spades'),
        Card('4', 'spades'),
        Card('5', 'spades'),
        Card('K', 'diamonds'),
        Card('A', 'hearts')
    ]

    allP1cards = river + p1.hand
    allP2cards = river + p2.hand

    return p1, p2, allP1cards, allP2cards, river

def test_ReturnFlush(setup_players_and_river):
    _, _, allP1cards, _, _ = setup_players_and_river
    assert ReturnFlush(allP1cards) == True

def test_ReturnStraight(setup_players_and_river):
    _, _, allP1cards, _, _ = setup_players_and_river
    assert ReturnStraight(allP1cards) == True

def test_ReturnPair():
    combination = [Card('3', 'hearts'), Card('3', 'spades'), Card('5', 'diamonds'), Card('7', 'clubs'), Card('9', 'hearts')]
    assert ReturnPair(combination) == True

def test_ReturnTriple():
    combination = [Card('3', 'hearts'), Card('3', 'spades'), Card('3', 'diamonds'), Card('7', 'clubs'), Card('9', 'hearts')]
    assert ReturnTriple(combination) == True

def test_ReturnFourOfAKind():
    combination = [Card('3', 'hearts'), Card('3', 'spades'), Card('3', 'diamonds'), Card('3', 'clubs'), Card('9', 'hearts')]
    assert ReturnFourOfAKind(combination) == True

def test_ReturnFullHouse():
    combination = [Card('3', 'hearts'), Card('3', 'spades'), Card('3', 'diamonds'), Card('7', 'clubs'), Card('7', 'hearts')]
    assert ReturnFullHouse(combination) == True

def test_StrongestSingleCard():
    combinations = [
        [Card('2', 'hearts'), Card('3', 'spades'), Card('5', 'diamonds'), Card('7', 'clubs'), Card('9', 'hearts')],
        [Card('2', 'hearts'), Card('4', 'spades'), Card('5', 'diamonds'), Card('8', 'clubs'), Card('K', 'hearts')]
    ]
    assert StrongestSingleCard(combinations) == combinations[1]

def test_ReturnStrongestHand(setup_players_and_river):
    p1, p2, allP1cards, allP2cards, _ = setup_players_and_river
    assert ReturnStrongestHand(allP1cards, p1) == [Card('2', 'spades'), Card('3', 'spades'), Card('4', 'spades'), Card('5', 'spades'), Card('6', 'spades')]
    assert ReturnStrongestHand(allP2cards, p2) == [Card('2', 'spades'), Card('3', 'spades'), Card('4', 'spades'), Card('5', 'spades'), Card('7', 'spades')]

def test_ReturnWinner(setup_players_and_river):
    p1, p2, allP1cards, allP2cards, _ = setup_players_and_river

    # Determine the strongest hand for both players
    PlayersStrongestHand = {
        p1.name: ReturnStrongestHand(allP1cards, p1),
        p2.name: ReturnStrongestHand(allP2cards, p2)
    }

    # Determine the winner
    assert ReturnWinner([p1, p2], PlayersStrongestHand) == ["P1"]

if __name__ == "__main__":
    pytest.main()
