# By Nathan Steward - 2-5-17
# This program reads in temperature data and calculates:
#   - The average deviation from the temperature anomaly in the first
#     x% of years in the file.
#   - The positive temperature anomaly in the first x% of years 
#     in the file.
#   - The average deviation from the temperature anomaly in the last
#     y% of years in the file.
#   - The positive temperature anomaly in the last y% of years 
#     in the file.
#     
#     Where X is the user's entered early split and Y is the calculated later split.
#     I.E. User enters '30' when asked, and receives first 30% of years data and last 70% of years data.

import Epic, math

# Method readTemps() reads the temperatures
# from the file and returns them in a list.
# Params: none
# Returns: an array of all temperatures from the file.
def readTemps():
    temps = []
    file = open('temps.txt', 'r')
    for line in file:
        temps.append(float(line))
    return temps

# Method calculateAve() calculates the average
# of a range of numbers.
# Params: temps, the list of temperatures.
#         start, the start index of the range.
#         stop, the end index of the range.
# Returns: the average of the range of numbers.
def calculateAve(temps, start, stop):
    sum = 0.0;
    for i in range(start, stop):
        sum += temps[i]
    return sum / (start - stop)
    
# Method count() counts all values that have a
# positive deviation in the range.
# Params: temps, the list of temperatures
#         start, the start index of the range.
#         stop, the end index of the range.
# Returns: the number of temperatures above
#          positive deviation.
def count(temps, start, stop):
    positiveTemps = []
    for i in range(start, stop):
        if temps[i] > 0.0:
            positiveTemps.append(temps[i])
    return len(positiveTemps)
    
# Method askUserForPercentageSplit() will prompt the user to
# enter an integer number to split the temperature readings with.
# For example: entering '20' will display the first 20% of readings
# contrasted with the last 80% of readings.
# Params: none
# Returns: the integer the user entered.
def askUserForPercentageSplit():
    repeating = True
    while repeating:
        try:
            earlySplit = Epic.userInt("What is the percentage of early years you wish to contrast with later years? (eg Enter '70' to view first 70 percent and last 30 percent): ")
            if earlySplit == 0:
                print "Your number needs to be larger than 0!"
            elif earlySplit >= 100 or earlySplit < 0:
                print "Oops, that number was too big or too small. Try something above 0 and under 100."
            else:
                print "\n"
                repeating = False
        except ValueError:
            print "Oops, that was not a proper integer. Try a number like '25' or '60'."
    return earlySplit
    
# Methoid main() runs all of the other methods necessary to 
# accomplish the intended function of the program.
# Params: none
# Returns: none
def main():
    temps = readTemps()
    
    earlySplit = askUserForPercentageSplit()
    lateSplit = 100.0 - earlySplit
    
    # In earlyYears and laterYears:
    #   - We are turning a percentage into a number of years with (length*split)/100.
    #   - That float is rounded and then turned into an integer.
    earlyYears = int(round((len(temps)*earlySplit)/100))
    laterYears = int(round((len(temps)*lateSplit)/100))
    
    earlyAvg = calculateAve(temps, 0, earlyYears)
    earlyNumYearsPositive = count(temps, 0, earlyYears)
    
    lateAvg = calculateAve(temps, earlyYears, len(temps))
    lateNumYearsPositive = count(temps, earlyYears, len(temps))
    
    print "During the first %i years, the average deviation from the temperature anomaly is %.12f." % (earlyYears, earlyAvg)
    print "During the first %i years, %i had a positive temperature anomaly." % (earlyYears, earlyNumYearsPositive)
    print "During the last %i year(s), the average deviation from the temperature anomaly is %.12f." % (laterYears, lateAvg)
    print "During the last %i year(s), %i had a positive temperature anomaly." % (laterYears, lateNumYearsPositive)

# Run program
main()