class Cards:
    suit_emojis = {
        "spades": "♠️"
        "hearts": "♥️"
        "clubs": "♣️"
        "diamonds": "♦️"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit_emoji = self.suit_emojis[f"{self.suit}"]
        return f"{self.rank}{suit_emoji}"

card = Cards(10, hearts)
print(card)
