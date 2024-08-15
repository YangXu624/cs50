class Card:
    suit_emojis = {
        'hearts': '\u2665',
        'diamonds': '\u2666',
        'clubs': '\u2663',
        'spades': '\u2660'
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit_emoji = self.suit_emojis.get(self.suit, '')
        return f"{self.rank}{suit_emoji}"

    def __repr__(self):
        return self.__str__()

    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)
