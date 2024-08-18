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

def StrongestPair(StoredPair):
    RankOfCards = []
    for PairCombination in StoredPair:
        RankOfCombination = []
        for card in PairCombination:
            RankOfCombination.append(card.rank)
        RankOfCards.append(RankOfCombination)
    count = {}
    for PairCombination in RankOfCards:
        for card in PairCombination:
            if card in count:
                count[item] += 1
            else:
                count[item] = 1

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
