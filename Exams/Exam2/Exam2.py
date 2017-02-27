# Exam 2 by Nathan Steward for Python
#  - Takes entries from 'timings.txt' file
#  - Displays the person's name (token 0) in a category
#    respective of how quickly they finished a rubiks
#    cube (token 1).

# Function initiateValues
#   - No arguments
#   - Returns an array of the time arrays
def initiateValues():
    file = open('timings.txt', 'r')
    timesPathetic = []
    timesAverage = []
    timesIntermediate = []
    timesAdvanced = []
    timesSquareMaster = []
    timesCubeHead = []
    
    for line in file:
        timing = line.split(", ")
        if float(timing[1]) < 10.0:
            timesCubeHead.append(timing[0])
        elif float(timing[1]) >= 10.0 and float(timing[1]) < 20.0:
            timesSquareMaster.append(timing[0])
        elif float(timing[1]) >= 20.0 and float(timing[1]) < 30.0:
            timesAdvanced.append(timing[0])
        elif float(timing[1]) >= 30.0 and float(timing[1]) < 40.0:
            timesIntermediate.append(timing[0])
        elif float(timing[1]) >= 40.0 and float(timing[1]) < 60.0:
            timesAverage.append(timing[0])
        else:
            timesPathetic.append(timing[0])
    times = [timesCubeHead, timesSquareMaster, timesAdvanced, 
            timesIntermediate, timesAverage, timesPathetic]
    return times

# Function initiatePrompts
#   - No arguments
#   - Returns an array of strings that will be used when printing results
def initiatePrompts():
    return ["\nCube Head (0-9.99):",
            "\nSquare Master (10-19.99):",
            "\nAdvanced Twister (20-29.99):",
            "\nIntermediate Turner(30-39.99):",
            "\nAverage Mover (40-59.99):",
            "\nPathetic (60 and beyond):"]

# Function displayResults
#   - 2 arguments
#       - times, the array of people's names for a certain time range
#       - prompt, a string that describes the category of the people within
#         the array
#   - Returns nothing
def displayResults(times, prompt):
    print prompt
    for name in times:
        print "\t%s" % name

# Function main
#   - No arguments
#   - Returns nothing
def main():
    allTimes = initiateValues()
    promptArray = initiatePrompts()
    for i in range(0, len(allTimes)):
        displayResults(allTimes[i], promptArray[i])

# Run program
main()
    