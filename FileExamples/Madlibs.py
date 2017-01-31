import Epic

def getUserInputs():
    adjective1 = Epic.userString("Enter an adjective: ")
    adjective2 = Epic.userString("Enter another adjective: ")
    pluralnoun1 = Epic.userString("Enter a plural noun: ")
    pluralnoun2 = Epic.userString("Enter another plural noun: ")
    celebrity = Epic.userString("Enter a celebrity: ")
    noun = Epic.userString("Enter a noun: ")
    print
    compendium = [adjective1, adjective2, pluralnoun1, pluralnoun2, celebrity, noun]
    return compendium

def compileMadLibs(words):
    print "Today I felt %s, so I decided to look for a %s with the local %s. We were terribly surprised to find a bunch of %s surrounding big-time star %s! From our angle, it looked like the big-shot was %s." % (words[0], words[5], words[2], words[3], words[4], words[1])

madLibWords = getUserInputs()
compileMadLibs(madLibWords)