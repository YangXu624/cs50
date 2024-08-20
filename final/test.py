from cards import Card
from random import choice
from players import Player
from bot import Bot
from evaluate import ReturnStrongestHand, ReturnWinner


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
    bot1= Bot(name="Bot 1")
    players.append(bot1)
    no_of_players = len(players)


    #Initiate pot
    pot = 0


    #MANUALLY DEAL PLAYER1 HIS HAND
    player1.hand = []
    card21 = Card('6', 'spades')
    card22 = Card('9', 'spades')
    player1.hand.append(card21)
    player1.hand.append(card22)

    #MANUALLY DEAL BOT1 HIS HAND
    bot1.hand = []
    card10 = Card('6', 'spades')
    card20 = Card('7', 'spades')
    bot1.hand.append(card10)
    bot1.hand.append(card20)

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

    #MANUALLY SET RIVER
    river = []
    card1 = Card('1', 'spades')
    card2 = Card('2', 'spades')
    card3 = Card('3', 'spades')
    card4 = Card('4', 'spades')
    card5 = Card('5', 'spades')
    river.append(card1)
    river.append(card2)
    river.append(card3)
    river.append(card4)
    river.append(card5)
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

        print("before strongesthand")
    #Iterate through players, appends dictionary as such: {'PLAYERNAME': [PLAYERSTRONGESTHAND]}
    PlayersStrongestHand = {}
    for player in players:
        allPlayerCards = river + player.hand
        PlayersStrongestHand[player.name] = ReturnStrongestHand(allPlayerCards, player)

    print("before returnwinner")
    #Returns a list of players who share the STRONGEST HANDSTRENGTH
    winner_list = ReturnWinner(players, PlayersStrongestHand)
    #If there is only 1 player with the strongest hand, he is the winner
    if len(winner_list) == 1:
        print(f"Winner is {winner_list[0]}!")
    #Else, REQUIRE FUNCTION TO COMPARE WITHIN ONE HANDSTRENGTH TIER
    #Can access players' strongest hand using dictionary 'PlayersStrongestHand'
    else:
        print(f"Winners are {winner_list}")

    #Require a function that returns winner

    #Pseudocode: winner.balance += pot then reset pot to 0

    #Reveal bot's hand
    for player in players:
        print(f"{player.name}'s hand was {player.hand}, forming a strongest handstrength of {PlayersStrongestHand[player.name]}")


def main():
    game()


if __name__ == "__main__":
    main()
