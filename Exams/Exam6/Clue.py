################################################################################
#   Nathan Steward, Exam 6, Python Spring 2017
#   Clue - A useful tool that helps you narrow down the killer in the game!
################################################################################

import Epic

################################################################################
#   Main() - Run the main program.
#   - Initializes the lists of weapons and suspects.
#   - Loops through clues while there is more than 1 possibility.
#   - Allows user to enter in the type of clue received.
#   - With the handleUserInput function, we select a single suspect or 
#   weapon and remove them from the list.
#   - When there is only one possibility left, the loop breaks and whoDidIt runs.
################################################################################
def main():
    weapons = ['Candlestick', 'Wrench', 'Pipe']
    suspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
    overOnePossibility = True
    while overOnePossibility:
        print "\n%s possibilities left." % (len(weapons)*len(suspects))
        
        clueType = ""
        while str.upper(clueType) != "W" and str.upper(clueType) != "S":
            clueType = Epic.userString("Is the clue about a weapon or a suspect (w or s)? ")
        
        toBeRemoved = handleUserInput(str.upper(clueType), suspects, weapons)
        
        if str.upper(clueType) == "S":
            for index in range(0, len(suspects)):
                if str.upper(toBeRemoved) == str.upper(suspects[index]):
                    del suspects[index]
                    break
        elif str.upper(clueType) == "W":
            for index in range(0, len(weapons)):
                if str.upper(toBeRemoved) == str.upper(weapons[index]):
                    del weapons[index]
                    break
        
        overOnePossibility = continuePlaying(weapons, suspects)
    whoDidIt(weapons[0], suspects[0])

################################################################################
#   Ends the loop and runs the print function if only 1 possibility remains.
################################################################################
def continuePlaying(weapons, suspects):
    if (len(weapons)*len(suspects)) > 1:
        return True
    return False
    
################################################################################
#   Handles the user input based on what type of clue the user received.
################################################################################
def handleUserInput(clueType, suspects, weapons):
    loopThis = True
    innocentOrUnused = ""
    if clueType == "W":
        while loopThis:
            innocentOrUnused = Epic.userString("Enter the weapon that was not used (%s)" % weapons)
            for weapon in weapons:
                if str.upper(innocentOrUnused) == str.upper(weapon):
                    loopThis = False
    elif clueType == "S":
        while loopThis:
            innocentOrUnused = Epic.userString("Enter the innocent suspect (%s)" % suspects)
            for suspect in suspects:
                if str.upper(innocentOrUnused) == str.upper(suspect):
                    loopThis = False
    else:
        raise Exception("Something went wrong!")
    return innocentOrUnused

################################################################################
#   Prints who killed and their respective weapon.
################################################################################
def whoDidIt(weapon, suspect):
    print "\nIt was %s with the %s!" % (suspect, weapon)

################################################################################
#   Run the main program.
################################################################################
main()