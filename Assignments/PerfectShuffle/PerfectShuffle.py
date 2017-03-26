import Epic
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck = []
    for i in range(0, len(rank)):
        for j in range(0, len(suit)):
            deck.append("%s of %s" % (rank[i], suit[j]))
    return deck

def shuffle(deck):
    half1 = deck[0:26]
    half2 = deck[26:]
    newDeck = []
    for i in range(0, len(half1)):
        newDeck.append(half1[i])
        newDeck.append(half2[i])
    return newDeck

def deal(deck):
    return deck[0:5]

def main():
    deck = buildDeck(rank, suit)
    timesShuffle = Epic.userInt("How many times do you want me to shuffle? ")
    for i in range(0, timesShuffle):
        deck = shuffle(deck)
    print deal(deck)

main()