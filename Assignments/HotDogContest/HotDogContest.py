################################################################################
#   Nathan Steward
#   2-28-17
#   HotDogContest.py
#   -Runs a hotdog eating contest! Bet on one of three participants
#   at a chance for glory and cash!
################################################################################

import Epic
import time
import random

################################################################################
#   -Function main()
#   -Runs the program
#   -Returns nothing
################################################################################
def main():
    cash = 100
    while cash > 0:
        contestants = {"Tom" : 0, "Sally" : 0, "Fred" : 0}
        betTarget = getBetTarget()
        bet = setBet(cash)
        contestants = runCompetition(contestants)
        cash += declareVictor(contestants, betTarget, bet)
    print "You're all out of money!!! Come back when you have some more!"

################################################################################
#   -Function getBetTarget()
#   -Asks user to provide the name of the target they're betting will win.
#   -Only resolves when the user enters a correct name in any lettercase.
#   -Returns betTarget, the name of the contestant
################################################################################
def getBetTarget():
    incorrectBetTarget = True
    while incorrectBetTarget:
        betTarget = str.capitalize(
            Epic.userString("Pick a winner (Tom, Sally, or Fred): ").lower()
            )
        if (betTarget == "Tom" or betTarget == "Sally" or betTarget == "Fred"):
            return betTarget
        else:
            print "Please bet on somebody who's actually eating!"
    return False

################################################################################
#   -Function setBet(int cash)
#   -Asks user to provide an amount they would like to bet
#   -Only resolves when the user enters a correct amount (between 1 and
#   their max amount of currently held cash)
#   -Returns bet, the int amount entered that the user is betting
################################################################################
def setBet(cash):
    stillBetting = True
    bet = 0
    while stillBetting:
        bet = Epic.userInt("How much do you want to bet? (Cash = %i)" % cash)
        if bet > cash:
            print "You can't bet more money than you have!"
        elif bet <= 0:
            print "You can't bet nothing or a negative number!"
        else:
            stillBetting = False
    return bet

################################################################################
#  -Function runCompetition(Dictionary contestants)
#  -Runs every round of the Hot Dog Contest until it is finished.
#  -Over the course of the competition, each contestant key in the contestants 
#   dictionary will have their value (hotdogs eaten) increased.
#  -Returns contestants, the dictionary of contestants and their hotdogs eaten
################################################################################
def runCompetition(contestants):
    mostHotdogsEaten = 0
    print "Ready, set, eat!"
    while mostHotdogsEaten < 50:
        print "\nchomp...  chomp...  chomp...\n"
        for contestant in contestants:
            contestants[contestant] += random.randrange(1, 6)
            if contestants[contestant] > mostHotdogsEaten:
                mostHotdogsEaten = contestants[contestant]
            print "%s has eaten %i hot dogs!" % (contestant, contestants[contestant])
        time.sleep(1)
    return contestants

################################################################################
#  -Function declareVictor(Dictionary contestants, String betTarget, int bet)  
#  -Inspects each contestant's victory conditions:
#       - If the contestant isn't in a winning condition, he loses.
#       - If the contestant is in the winning condition...
#           - ... if there is no other person in a winning condition, they win.
#           - ... if there is another person in a winning condition, it's a tie.
#  -Returns the amount of money the user won (or lost)
################################################################################
def declareVictor(contestants, betTarget, bet):
    if contestants[betTarget] < 50:
        print "\nOh no, you aren't top dog! ",
        print "Maybe you should train harder! You lost %i cash.\n" % bet
        return -bet
    elif contestants[betTarget] >= 50:
        tie = False
        for contestant in contestants:
            if contestants[contestant] >= 50 and contestant != betTarget:
                tie = True
        if tie:
            print "\nIt's a tie! You got your money back!\n"
            return 0
        else:
            print "\nWell hot dog, you're the Hot Dog champion! ", 
            print "You won %i cash!\n" % bet
            return bet

main()