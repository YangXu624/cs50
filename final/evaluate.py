from itertools import combinations

def ReturnFlush(combination):
    r = all(combination[i].suit == combination[0].suit for i in range(1, len(combination)))
    if r == True:
        return combination


def ReturnStraight(combination):
    CardValues = []
    for card in combination:
        if card.rank == "J":
            card.rank = 11
        elif card.rank == "Q":
            card.rank = 12
        elif card.rank == "K":
            card.rank = 13
        elif card.rank == "A":
            card.rank = 14
        CardValues.append(int(card.rank))
    CardValues.sort()
    previous = CardValues[0]
    checkAllIncrements = []
    for number in CardValues[1:]:
        if previous == number - 1:
            previous = number
            checkAllIncrements.append(True)
        else:
            checkAllIncrements.append(False)
    r = all(checkAllIncrements)
    if r == True:
        return combination


def ReturnPair(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    if 2 == InstancesOfValue.count(2) and 3 == InstancesOfValue.count(1):
        return combination


def ReturnTriple(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    if 3 == InstancesOfValue.count(3) and 2 == InstancesOfValue.count(1):
        return combination


def ReturnFourOfAKind(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    if 4 == InstancesOfValue.count(4):
        return combination


def ReturnTwoPair(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    if 4 == InstancesOfValue.count(2):
        return combination


def ReturnFullHouse(combination):
    RankOfCards = []
    for card in combination:
        RankOfCards.append(card.rank)
    InstancesOfValue = []
    for value in RankOfCards:
        NumberOfRepeats = RankOfCards.count(value)
        InstancesOfValue.append(NumberOfRepeats)
    if 2 == InstancesOfValue.count(2) and 3 == InstancesOfValue.count(3):
        return combination


def StrongestPair(StoredPair):
    if StoredPair == []:
        return
    RankOfCards = []
    for PairCombination in StoredPair:
        RankOfCombination = []
        for card in PairCombination:
            RankOfCombination.append(card.rank)
        RankOfCards.append(RankOfCombination)
    ListOfSum = []
    for PairCombination in RankOfCards:
        Count = {}
        sum = 0
        for card in PairCombination:
            if card in Count:
                Count[card] += 1
            else:
                Count[card] = 1
        for item in Count:
            if Count[item] != 2:
                sum += int(item)
        ListOfSum.append(sum)
    print(ListOfSum)
    HighestSum = 0
    for sum in ListOfSum:
        if sum > HighestSum:
            HighestSum = sum
    IndexOfStrongestPair = ListOfSum.index(HighestSum)
    return StoredPair[IndexOfStrongestPair]


def ReturnStrongestHand(allPlayerCards, player):
    allCombinations = combinations(allPlayerCards, 5)
    best_hand = []
    #List containing all pair combinations
    list_of_pairs = []
    highest_strength = 1  # Default hand strength (High Card)

    for combination in allCombinations:
        if ReturnFourOfAKind(combination):
            current_strength = 8
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnFullHouse(combination):
            current_strength = 7
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnFlush(combination):
            current_strength = 6
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnStraight(combination):
            current_strength = 5
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnTriple(combination):
            current_strength = 4
            if current_strength > highest_strength:
                best_hand = combination
                highest_strength = current_strength

        elif ReturnTwoPair(combination):
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

        if highest_strength == 2:
            best_hand = StrongestPair(list_of_pairs)

    player.handstrength = highest_strength
    return best_hand if best_hand else player.hand


def ReturnWinner(players):
    score = 0
    winners = []

    for player in players:
        if player.handstrength > score:
            winners = [player.name]  # Start a new winners list
            score = player.handstrength
        elif player.handstrength == score:
            winners.append(player.name)  # Add to the existing winners list

    return winners
