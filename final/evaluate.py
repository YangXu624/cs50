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
    StoredFlush = []
    StoredStraight = []
    StoredFullHouse = []
    StoredFourOfAKind = []
    StoredPair = []
    StoredTriple = []
    StoredTwoPair = []
    for combination in allCombinations:
        FourOfAKind = ReturnFourOfAKind(combination)
        if FourOfAKind != None:
            StoredFourOfAKind.append(FourOfAKind)
            player.handstrength = 8
            return StoredFourOfAKind

        FullHouse = ReturnFullHouse(combination)
        if FullHouse != None:
            StoredFullHouse.append(FullHouse)
            player.handstrength = 7
            return StoredFullHouse

        Flush = ReturnFlush(combination)
        if Flush != None:
            StoredFlush.append(Flush)
            player.handstrength = 6
            return StoredFlush

        Straight = ReturnStraight(combination)
        if Straight != None:
            StoredStraight.append(Straight)
            player.handstrength = 5
            return StoredStraight

        Triple = ReturnTriple(combination)
        if Triple != None:
            StoredTriple.append(Triple)
            player.handstrength = 4
            return StoredTriple

        TwoPair = ReturnTwoPair(combination)
        if TwoPair != None:
            StoredTwoPair.append(TwoPair)
            player.handstrength = 3
            return StoredTwoPair

        Pair = ReturnPair(combination)
        if Pair != None:
            StoredPair.append(Pair)
            player.handstrength = 2
            return StoredPair

    player.handstrength = 1
    return []


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
