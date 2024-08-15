from cards import Card
from random import choice
from players import Player
from bot import Bot


#Argument river(list) and deck(list), returns an updated river and deck
def round(river, deck):
    #Add one card to the river
    card = choice(deck)
    river.append(card)
    deck.remove(card)
    return river, deck


#Argument player and current bet, returns player's bet
def bet(player, current):
    initial = player.balance
    #Perform action: Call/check/raise by n/fold
    player.balance = player.action(current)
    added_to_pot = initial - player.balance
    return added_to_pot


def main():
    #Create deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)

    #Add players into a list called 'players'
    players = []
    #Add user into game
    player1 = Player(name="Player 1")
    players.append(player1)
    #Add bot into game
    bot = Bot(name="Bot")
    players.append(bot)

    #Initiate pot
    pot = 0

    #Deal hands
    for player in players:
        for i in range(2):
            player.hand[i] = choice(deck)
            deck.remove(player.hand[i])

    #Tell user his hand
    print(f"\nYour hand is {player1.hand}\n")

    #Pre-river betting
    #Current = Minimum bet
    current1 = 2
    #Each player takes turns to perform action
    for player in players:
        added = bet(player, current1)
        print(f"{player.name} balance: {player.balance}")
        current1 = added
        pot += added
        print(f"Pot value: {pot}\n")

    #Iterate rounds
    river = []
    for i in range(5):
        print(f"Round {i + 1}")
        #Deal a card to the river
        river, deck = round(river, deck)
        print(f"River: {river}")

        #Current = Minimum bet
        current2 = 0
        #Each player takes turns to perform action
        for player in players:
            added = bet(player, current2)
            print(f"{player.name} now has {player.balance}")
            current2 = added
            pot += added
            print(f"Pot value: {pot}\n")

    #TBC: Evaluate and compare hand strength to determine winner

    #Reveal bot's hand
    print(f"Bot's hand was {bot.hand}")

if __name__ == "__main__":
    main()
