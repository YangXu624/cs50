from emoji import emojize

class Cards:
    suit_emojis = {
        'Hearts': ':',
        'Diamonds': '\u2666',
        'Clubs': '\u2663',
        'Spades': '\u2660'
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit_emoji = self.suit_emojis.get(self.suit, ' ')
        return f"{self.rank}{suit_emoji}"

card = Cards(10, "hearts")
print(card)
