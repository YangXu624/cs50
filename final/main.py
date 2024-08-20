from cards import Card
from random import choice
from players import Player
from bot import Bot
from evaluate import ReturnStrongestHand, ReturnWinner, ConvertJQKA


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



def game(players_list):
    #Create deck
    deck = []
    for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(rank, suit)
            deck.append(card)


    #Add players into a list called 'players'
    players = players_list
    no_of_players = len(players)
    #You are Player 1
    player1 = players_list[0]


    #Initiate pot
    pot = 0


    #Deal hands
    for player in players:
        for i in range(2):
            card = choice(deck)
            player.hand.append(card)
            deck.remove(card)


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


    #Iterate through players, appends dictionary as such: {'PLAYERNAME': [PLAYERSTRONGESTHAND]}
    PlayersStrongestHand = {}
    for player in players:
        allPlayerCards = river + player.hand
        PlayersStrongestHand[player.name] = ReturnStrongestHand(allPlayerCards, player)

    #Returns a list of players who share the STRONGEST HANDSTRENGTH
    winner_list = ReturnWinner(players,PlayersStrongestHand)
    #If there is only 1 player with the strongest hand, he is the winner
    if len(winner_list) == 1:
        winner = winner_list[0]
        print(f"Winner is {winner}!\n")
        winner.balance += pot
        pot = 0

    else:
        no_of_winners = len(winner_list)
        split_pot = int(pot / no_of_winners)
        print(f"Winners are {winner_list}")

        for winner in winner_list:
            winner.balance += split_pot

    #Convert card.rank from int back to J Q K A
    for player in players:
        ConvertJQKA(player.hand)
    ConvertJQKA(PlayersStrongestHand[player.name])

    #Reveal bot's hand
    for player in players:
        print(f"{player.name}'s hand was {player.hand}, forming a strongest handstrength of {PlayersStrongestHand[player.name]}")


def main():
    games = int(input("Number of games: "))
    bal = int(input("Player Balance: "))
    bot = int(input("Number of Bots: "))

    players_list = []
    #Add user into game
    player1 = Player(name="Player 1", balance=bal)
    players_list.append(player1)

    #Add bot into game
    for i in range(bot):
        bot = Bot(name=f"Bot {i}", balance=bal)
        players_list.append(bot)

    for i in range(games):
        game(players_list)


if __name__ == "__main__":
    main()
