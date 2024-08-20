from itertools import combinations

# Returns count of combination e.g Combination['J', 'K', 'K', '1', 'K'] returns [1, 3, 3, 1, 3]
def Instances(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    return InstancesOfValue

# Returns True if FLUSH
def ReturnFlush(combination):
    return all(combination[i].suit == combination[0].suit for i in range(1, len(combination)))


# Returns True if STRAIGHT
def ReturnStraight(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    RankOfCards.sort()
    previous = RankOfCards[0]
    checkAllIncrements = []
    for number in RankOfCards[1:]:
        if previous == number - 1:
            previous = number
            checkAllIncrements.append(True)
        else:
            checkAllIncrements.append(False)
    return all(checkAllIncrements)

# Returns True if PAIR
def ReturnPair(combination):
    repeats = Instances(combination)
    if 2 == repeats.count(2) and 3 == repeats.count(1):
        return True

# Returns True if TRIPLE
def ReturnTriple(combination):
    repeats = Instances(combination)
    if 3 == repeats.count(3) and 2 == repeats.count(1):
        return True

# Returns True if FOUR OF A KIND
def ReturnFourOfAKind(combination):
    repeats = Instances(combination)
    if 4 == repeats.count(4):
        return True

# Returns True if TWO PAIR
def ReturnTwoPair(combination):
    repeats = Instances(combination)
    if 4 == repeats.count(2):
        return True

# Returns True if FULL HOUSE
def ReturnFullHouse(combination):
    repeats = Instances(combination)
    if 2 == repeats.count(2) and 3 == repeats.count(3):
        return True


def StrongestSingleCard(Combinations):
    ListOfSum = []
    print("COMBINATIONS: ", Combinations)
    for combination in Combinations:
        Count = {}
        sum = 0
        for card in combination:
            if card.rank in Count:
                Count[card.rank] += 1
            else:
                Count[card.rank] = 1
        for item in Count:
            if Count[item] == 1:
                sum += item
        ListOfSum.append(sum)
    HighestSum = 0
    for sum in ListOfSum:
        if sum > HighestSum:
            HighestSum = sum
    indexOfStrongestSingle = ListOfSum.index(HighestSum)
    print("Winning hand is", Combinations[indexOfStrongestSingle])
    return Combinations[indexOfStrongestSingle]

def HasStrongestPair(HasPairCombination):
    largestPairCardInEachCombi = []
    for combination in HasPairCombination:
        seen = []
        duplicate = []
        for card in combination:
            if card.rank in seen:
                duplicate.append(card.rank)
            else:
                seen.append(card.rank)
        largestPairCard = 0
        for tempLargestPairCard in duplicate:
            if tempLargestPairCard > largestPairCard:
                largestPairCard = tempLargestPairCard
        largestPairCardInEachCombi.append(largestPairCard)
    largestPairNumber = 0
    for tempLargestPairNumber in largestPairCardInEachCombi:
        if tempLargestPairNumber > largestPairNumber:
            largestPairNumber = tempLargestPairNumber
    indexesOfCombiWithLargestPair = [i for i, x in enumerate(largestPairCardInEachCombi) if x == largestPairNumber]
    CombiHasStrongestPair = []
    for index in indexesOfCombiWithLargestPair:
        CombiHasStrongestPair.append(HasPairCombination[index])
    return CombiHasStrongestPair

def HasSecondStrongestPair(HasStrongestPair):
    ListOfSum = []
    for combination in HasStrongestPair:
        Count = {}
        sum = 0
        for card in combination:
            if card.rank in Count:
                Count[card.rank] += 1
            else:
                Count[card.rank] = 1
        for item in Count:
            if Count[item] == 2 or Count[item] == 4:
                sum += item
        ListOfSum.append(sum)
    HighestSum = 0
    for sum in ListOfSum:
        if sum > HighestSum:
            HighestSum = sum
    indexesOfStrongTwoPair = [i for i, x in enumerate(ListOfSum) if x == HighestSum]
    StrongTwoPair = []
    for index in indexesOfStrongTwoPair:
        StrongTwoPair.append(HasStrongestPair[index])
    return StrongTwoPair

def HasStrongestTripleForFullHouse(HasStrongestPair):
    ListOfSum = []
    for combination in HasStrongestPair:
        Count = {}
        sum = 0
        for card in combination:
            if card.rank in Count:
                Count[card.rank] += 1
            else:
                Count[card.rank] = 1
        for item in Count:
            if Count[item] == 3:
                sum += item
        ListOfSum.append(sum)
    HighestSum = 0
    for sum in ListOfSum:
        if sum > HighestSum:
            HighestSum = sum
    indexOfStrongestTriple = ListOfSum.index(HighestSum)
    return HasStrongestPair[indexOfStrongestTriple]

def HasStrongestTriple(HasStrongestPair):
    ListOfSum = []
    for combination in HasStrongestPair:
        Count = {}
        sum = 0
        for card in combination:
            if card.rank in Count:
                Count[card.rank] += 1
            else:
                Count[card.rank] = 1
        for item in Count:
            if Count[item] == 3:
                sum += item
        ListOfSum.append(sum)
    HighestSum = 0
    for sum in ListOfSum:
        if sum > HighestSum:
            HighestSum = sum
    indexesOfTriple = [i for i, x in enumerate(ListOfSum) if x == HighestSum]
    Triple = []
    for index in indexesOfTriple:
        Triple.append(HasStrongestPair[index])
    return Triple

def ReturnStrongestHand(allPlayerCards, player):
    # change all card.rank to int
    for card in allPlayerCards:
        if card.rank == "J":
            card.rank = 11
        elif card.rank == "Q":
            card.rank = 12
        elif card.rank == "K":
            card.rank = 13
        elif card.rank == "A":
            card.rank = 14
        else:
            card.rank = int(card.rank)

    # Stores all 21 combinations in a list of tuples
    allCombinations = combinations(allPlayerCards, 5)

    # Changes allCombinations to a list of list
    NewAllCombinations = []
    for combination in allCombinations:
        NewAllCombinations.append(list(combination))

    #List containing combinations
    best_hand = []
    list_of_pairs = []
    list_of_twoPairs = []
    list_of_triples = []
    list_of_straight = []
    list_of_flush = []
    list_of_fullHouse = []
    list_of_fourOfAKind = []
    list_of_straightFlush = []
    # Default hand strength (High Card)
    highest_strength = 1

    for combination in NewAllCombinations:
        if ReturnFlush(combination) and ReturnStraight(combination):
            list_of_straightFlush.append(combination)
            current_strength = 9
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnFourOfAKind(combination):
            list_of_fourOfAKind.append(combination)
            current_strength = 8
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnFullHouse(combination):
            list_of_fullHouse.append(combination)
            current_strength = 7
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnFlush(combination):
            list_of_flush.append(combination)
            current_strength = 6
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnStraight(combination):
            list_of_straight.append(combination)
            current_strength = 5
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnTriple(combination):
            list_of_triples.append(combination)
            current_strength = 4
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnTwoPair(combination):
            list_of_twoPairs.append(combination)
            current_strength = 3
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnPair(combination):
            list_of_pairs.append(combination)
            current_strength = 2
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

    if highest_strength == 1:
        best_hand = StrongestSingleCard(NewAllCombinations)

    elif highest_strength == 2:
        best_hand = StrongestSingleCard(list_of_pairs)

    elif highest_strength == 3:
        CombiHasStrongestPair = HasStrongestPair(list_of_twoPairs)
        HasStrongestTwoPair = HasSecondStrongestPair(CombiHasStrongestPair)
        best_hand = StrongestSingleCard(HasStrongestTwoPair)

    elif highest_strength == 4:
        CombiHasStrongestTriple = HasStrongestTriple(list_of_triples)
        best_hand = StrongestSingleCard(CombiHasStrongestTriple)

    elif highest_strength == 5:
        best_hand = StrongestSingleCard(list_of_straight)

    elif highest_strength == 6:
        best_hand = StrongestSingleCard(list_of_flush)

    elif highest_strength == 7:
        HasLargestPair = HasSecondStrongestPair(list_of_fullHouse)
        best_hand = HasStrongestTripleForFullHouse(HasLargestPair)

    elif highest_strength == 8:
        HasLargestFourOfAKind = HasSecondStrongestPair(list_of_fourOfAKind)
        best_hand = StrongestSingleCard(HasLargestFourOfAKind)

    elif highest_strength == 9:
        best_hand == StrongestSingleCard(list_of_straightFlush)

    print(list_of_straightFlush)
    player.handstrength = highest_strength
    return best_hand


def ReturnWinner(players, PlayersStrongestHand):
    score = 0
    winners = []

    for player in players:
        if player.handstrength > score:
            winners = [player.name]  # Start a new winners list
            score = player.handstrength
        elif player.handstrength == score:
            winners.append(player.name)  # Add to the existing winners list

    if len(winners) == 1:
        return winners

    if len(winners) != 1:
        playersCombi = [] # list of Players best_hand of the same tier
        for player in players:
            if player.handstrength == score:
                playersCombi.append(PlayersStrongestHand[player.name])

    if score == 1 or score == 5 or score == 6 or score == 9:
        best_hand = StrongestSingleCard(playersCombi)

    elif score == 2:
        best_hand = StrongestSingleCard(HasStrongestPair(playersCombi))

    elif score == 3:
        CombiHasStrongestPair = HasStrongestPair(playersCombi)
        HasStrongestTwoPair = HasSecondStrongestPair(CombiHasStrongestPair)
        best_hand = StrongestSingleCard(HasStrongestTwoPair)

    elif score == 4:
        CombiHasStrongestTriple = HasStrongestTriple(playersCombi)
        best_hand = StrongestSingleCard(CombiHasStrongestTriple)

    elif score == 7:
        HasLargestPair = HasSecondStrongestPair(playersCombi)
        best_hand = HasStrongestTriple(HasLargestPair)

    elif score == 8:
        HasLargestFourOfAKind = HasSecondStrongestPair(playersCombi)
        best_hand = StrongestSingleCard(HasLargestFourOfAKind)

    best_hand_rank = []
    for card in best_hand:
        best_hand_rank.append(card.rank)

    list_of_winners = []
    for player in players:
        playerRank = []
        for card in PlayersStrongestHand[player.name]:
            playerRank.append(card.rank)
        if playerRank == best_hand_rank:
            list_of_winners.append(player.name)

    return list_of_winners

def ConvertJQKA(list):
        for card in list:
            if card.rank == 11:
                card.rank = "J"
            if card.rank == 12:
                card.rank = "Q"
            if card.rank == 13:
                card.rank = "K"
            if card.rank == 14:
                card.rank = "A"

if __name__ == "__main__":
    main()
