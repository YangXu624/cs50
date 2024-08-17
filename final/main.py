from cards import Card
from random import choice
from players import Player
from bot import Bot


#Argument: river and deck (which are both lists), returns an updated river and deck
def round(river, deck):
    #Add one card to the river
    card = choice(deck)
    river.append(card)
    deck.remove(card)
    return river, deck


#Argument: player and current bet, returns player's bet
def bet(player, current):
    initial = player.balance
    #Perform action: Call/check/raise by n/fold
    player.balance = player.action(current)
    added_to_pot = initial - player.balance
    return added_to_pot


def game():
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
    bot1, bot2 = Bot(name="Bot 1"), Bot(name="Bot 2")
    players.append(bot1)
    players.append(bot2)
    no_of_players = len(players)
    print(players)


    #Initiate pot
    pot = 0


    #Deal hands
    for player in players:
        for i in range(2):
            card = choice(deck)
            player.hand.append(card)
            deck.remove(card)
        print(player.name, player.hand)


    #Tell user his hand
    print(f"\nYour hand is {player1.hand}\n")


    #Pre-river betting
    #Current = Minimum bet
    current = 2
    #If a player raises, ensure everyone gets a turn to bet again, kept track by raise_count
    raised_count = 0
    #Initiate endround variable to end loop when round ends
    endround = False
    while endround == False:
        #Each player takes turns to perform action
        for player in players:
            if raised_count == no_of_players:
                endround = True
                break

            added = bet(player, current)
            player.current_bet += added
            print(f"{player.name} balance: {player.balance}")
            if player.current_bet > current:
                raised_count = 1
            else:
                raised_count += 1
            current = player.current_bet
            pot += added
            print(f"Pot value: {pot}\n")

    #Iterate rounds
    river = []
    for i in range(5):
        print(f"Round {i + 1}")
        #Deal a card to the river
        river, deck = round(river, deck)
        print(f"River: {river}")

        #Reset everyone's current bet to 0
        for player in players:
            player.current_bet = 0
        #Current = Minimum bet
        current = 0
        #If a player raises, ensure everyone gets a turn to bet again, kept track by raise_count
        raised_count = 0
        #Initiate endround variable to end loop when round ends
        endround = False
        while endround == False:
            #Each player takes turns to perform action
            for player in players:
                if raised_count == no_of_players:
                    endround = True
                    break

                added = bet(player, current)
                player.current_bet += added
                print(f"{player.name} balance: {player.balance}")
                if player.current_bet > current:
                    raised_count = 1
                else:
                    raised_count += 1
                current = player.current_bet
                pot += added
                print(f"Pot value: {pot}\n")

            if endround == True:
                break


    #TBC: Evaluate and compare hand strength to determine winner
    #Require a function that returns winner

    #Pseudocode: winner.balance += pot then reset pot to 0

    #Reveal bot's hand
    for player in players:
        print(f"{player.name}'s hand was {player.hand}")

#####################################################################################################
    winner = compare_hands(players)
    print(f"The winner is {winner.name} with the hand {winner.hand}")



from collections import Counter

def hand_rank(hand):
    """Evaluate the strength of a hand."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_values = {r: i for i, r in enumerate(ranks, 2)}
    rank_counts = Counter(card.rank for card in hand)
    suits = [card.suit for card in hand]
    rank_histogram = sorted(rank_counts.values(), reverse=True)
    sorted_ranks = sorted((rank_values[rank] for rank in rank_counts), reverse=True)

    # Check for flush (all cards of the same suit)
    flush = len(set(suits)) == 1
    # Check for straight (consecutive ranks)
    straight = len(rank_histogram) == 5 and (sorted_ranks[0] - sorted_ranks[-1] == 4)

    if flush and straight:
        return (8, sorted_ranks)  # Straight flush
    elif rank_histogram == [4, 1]:
        return (7, sorted_ranks)  # Four of a kind
    elif rank_histogram == [3, 2]:
        return (6, sorted_ranks)  # Full house
    elif flush:
        return (5, sorted_ranks)  # Flush
    elif straight:
        return (4, sorted_ranks)  # Straight
    elif rank_histogram == [3, 1, 1]:
        return (3, sorted_ranks)  # Three of a kind
    elif rank_histogram == [2, 2, 1]:
        return (2, sorted_ranks)  # Two pair
    elif rank_histogram == [2, 1, 1, 1]:
        return (1, sorted_ranks)  # One pair
    else:
        return (0, sorted_ranks)  # High card


def compare_hands(players):
    """Compare all players' hands to determine the winner."""
    player_ranks = [(player, hand_rank(player.hand)) for player in players]
    player_ranks.sort(key=lambda x: x[1], reverse=True)
    winner = player_ranks[0][0]
    return winner
############################################################################################


def main():
    game()


if __name__ == "__main__":
    main()
