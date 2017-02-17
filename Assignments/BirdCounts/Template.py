import Epic
# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# Also returns a dictionary of the top birds sighted.
# To return multiple dictionaries, we return one 'dictionary 
# of dictionaries', which we call the 'birdCompendium'.
# ------------------------------------------------------------
def countBirds(filename):
    birdCompendium = {} # Dictionary of dictionaries
    birdSightings = {}  # Dictionary of bird sightings
    mostSeenBirds = {}  # Dictionary of the top sighted birds
    mostSeen = 0        # Counter for the top number of times sighted for a bird
    
    for line in open("Birds.txt"):
        tokens = line.split(',')
        name = tokens[0].strip().lower()
        timesSeen = int(tokens[1].strip())
        
        # Adds to an existing bird's sight count if they already exist.
        if name in birdSightings:
            birdSightings[name] += timesSeen
        # Initialize the bird's sight count if they don't already exist.
        else:
            birdSightings[name] = timesSeen
            
        # See if the bird has set a record for number of times spotted;
        # if so, they're in the running to be the most sighted bird!
        if birdSightings[name] >= mostSeen:
            # Bird is spotted more than any other; it is alone in the 
            # list until we find others that either match it or surpass it.
            if birdSightings[name] > mostSeen:
                mostSeenBirds = {name : birdSightings[name]}
                mostSeen = birdSightings[name]
            # Bird is spotted as much as another bird; it is added
            # to the dictionary of current top record holders.
            else:
                mostSeenBirds[name] = birdSightings[name]

    # Compile the compendium of dictionaries and return them.
    birdCompendium = {"sightings" : birdSightings, "mostSeen" : mostSeenBirds}
    return birdCompendium

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# Also allows the user to exit the program by typing
# 'exit', and displays the top sighted birds.
# ------------------------------------------------------------
def askUser(d):
    # Run loop until user manually exits.
    running = True
    while running:
        # Accept user input.
        birdName = Epic.userString("Enter a bird name, or type 'exit' to quit: ")
        # If user typed 'exit', stop running.
        if birdName.lower() == "exit":
            running = False
            print "Happy spotting!"
            continue
        # If user typed in a bird that exists within the dictionary,
        # return the number of times that bird has been spotted.
        elif birdName.lower() in d["sightings"]:
            print "I have seen that bird %d time(s)." % d["sightings"][birdName]
        # If the user's bird cannot be found, return 0 times spotted.
        else:
            print "I have seen that bird 0 time(s)."
        # Print the list of the most seen birds.
        print "The most seen bird(s): "
        for birds in d["mostSeen"]:
            print " - %s, seen %d time(s)." % (birds.capitalize(), d["mostSeen"][birds])
            
def main():
    # Get the bird-related dictionaries.
    dictionaries = countBirds("Birds.txt")
    # Allow the user to interact with them.
    askUser(dictionaries) 

main()