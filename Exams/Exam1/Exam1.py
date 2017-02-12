# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    speeds = []
    file = open(filename, 'r')
    for line in file:
        speeds.append(int(line))
    return speeds
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    count = 0
    total = 0
    for number in l:
        count += 1
        total += number
    return total / (count * 1.0)
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    speedersCount = 0
    for speed in l:
        if speed > maxSpeed:
            speedersCount += 1
    return speedersCount
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    speedsRushHour = readData('data-rush.txt')
    speedsNotRushHour = readData('data-not-rush.txt')
    numSpeedersRushHour = countSpeeders(speedsRushHour, 69)
    numSpeedersNotRushHour = countSpeeders(speedsNotRushHour, 69)
    averageRushHour = getAverage(speedsRushHour)
    averageNotRushHour = getAverage(speedsNotRushHour)
    finesRushHour = numSpeedersRushHour * 150
    finesNotRushHour = numSpeedersNotRushHour * 100
    print "The average speed during rush hour was %.2f." % averageRushHour
    print "The average speed not during rush hour was %.2f." % averageNotRushHour
    print "There were %i speeders during rush hour. Total fine = $%i" % (numSpeedersRushHour, finesRushHour)
    print "There were %i speeders not during rush hour. Total fine = $%i" % (numSpeedersNotRushHour, finesNotRushHour)

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()