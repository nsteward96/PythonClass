import Epic
import random

choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']

################################################################################
#   main() - no arguments, returns nothing
#   - Runs the Concentration game. Takes in the user's input cards and performs
#   functions with them.
################################################################################
def main():
    deck = shuffleNewDeck()
    playing = True
    tries = 0
    while playing:
        tries += 1
        cardError = True
        while cardError:
            firstCard = Epic.userInt("Pick the first card to turn over (0-9): ")
            secondCard = Epic.userInt("Pick the second card to turn over (0-9): ")
            if firstCard == secondCard or firstCard > 9 or firstCard < 0 or secondCard > 9 or secondCard < 0:
                print "Invalid choices. You must pick different cards and the card must be a number from 0-9."
            else:
                cardError = False
        print "Card %d is a %s." % (firstCard, deck[firstCard])
        print "Card %d is a %s." % (secondCard, deck[secondCard])
        playing = checkWinCondition(deck, firstCard, secondCard, tries)
    
################################################################################
#   shuffleNewDeck() - no arguments, returns a shuffled deck ready for play
#   - Shuffles a new deck with an extra copy of one card in the deck so the 
#   user can find both cards and flip them up at the same time to win.
################################################################################
def shuffleNewDeck():
    dupeCard = choices[random.randrange(0, 9)]
    newCardSelections = choices
    newCardSelections.append(dupeCard)
    random.shuffle(newCardSelections)
    return newCardSelections

################################################################################
#   checkWinConditions() - 4 arguments (Array deck, Integer firstCard,
#                                       Integer secondCard, Integer tries)
#                        - Returns a boolean for if the game should continue
#   - Checks to see if the card in the deck at index firstCard is equal to
#   the card in the deck at index secondCard. If so, the user wins.
################################################################################
def checkWinCondition(deck, firstCard, secondCard, tries):
    returnStatement = True
    if deck[firstCard] == deck[secondCard]:
        returnStatement = False
        print "You win! It took you %d tries." % tries
    return returnStatement

# Runs the program.
main()