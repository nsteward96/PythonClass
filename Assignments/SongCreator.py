# Nathan Steward - 1-30-17
# Song Creator
# Allows you to enter 4 verses and a chorus. The chorus is repeated a number of times determined by the user.

import Epic

#################
# FUNCTIONS
#################

# Function getUserInput() takes information on the song's content from the user.
# Params: none
# Returns: list songInfo, containing all 4 verses, the chorus, and the number of times the chorus is repeated.
def getUserInput():
    # Accept user input
    verse1 = Epic.userString("Enter the first verse: ").upper()
    verse2 = Epic.userString("Enter the second verse: ").upper()
    verse3 = Epic.userString("Enter the third verse: ").upper()
    verse4 = Epic.userString("Enter the fourth verse: ").upper()
    chorus = Epic.userString("Enter the chorus: ").lower()
    try:
        chorusRepeat = Epic.userInt("Enter the chorus repeat: ")
    except ValueError:
        print
        print "! ERROR: A valid number was not entered. !"
        print
    
    # Filter out the cookies >:(
    verse1 = filterCookies(verse1)
    verse2 = filterCookies(verse2)
    verse3 = filterCookies(verse3)
    verse4 = filterCookies(verse4)
    chorus = filterCookies(chorus)
    
    songInfo = [verse1, verse2, verse3, verse4, chorus, chorusRepeat]
    
    return songInfo
    
    
# Function singSongHalf() prints out one half of the song. The song sings, twice, all 4 verses separated by the chorus, and sings an extra line of the chorus on the last run.
# To sing the whole song, singSongHalf() must be called twice.
# Params: list songInfo, containing all 4 verses, the chorus, and the number of times the chorus is repeated.
# Returns: none
def singSongHalf(songInfo):
    userSongVerses = [songInfo[0], songInfo[1], songInfo[2], songInfo[3]]
    userChorus = songInfo[4]
    userChorusRepeat = songInfo[5]
    for verse in userSongVerses:
        print
        print verse
        for i in range(0, userChorusRepeat):
            print "%s" % userChorus,
    print userChorus
    
    
# Function filterCookies() checks to see if the string contains the substring 'COOKIE'. If it does, the word is bleeped out by 6 underscores. Function commissioned by the country of Ubob.
# Params: String verse, words from the song (verse or chorus).
# Returns: String of words without the word 'cookie'.
def filterCookies(verse):
    verseTokens = verse.split(' ')
    for token in range(0, len(verseTokens)):
        if verseTokens[token].upper().find("COOKIE") >= 0:
            verseTokens[token] = "______" 
    return ' '.join(verseTokens)


##################
# MAIN
##################

userSongInfo = getUserInput()
singSongHalf(userSongInfo)
print
print "... one more time! ..."
singSongHalf(userSongInfo)