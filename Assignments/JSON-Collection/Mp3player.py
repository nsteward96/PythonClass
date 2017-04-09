import json
import Epic

def main():
    bands = getJson()
    userBand = Epic.userString("Enter a band name: ")
    searchForBand(bands, userBand)

def getJson():
    jsonText = ""
    file = open('songs.json')
    for line in file:
        line = line.strip()
        jsonText = jsonText + line
    bands = json.loads(jsonText)
    return bands

def searchForBand(bands, userBand):
    for band in bands:
        if band["Name"] == userBand:
            albumCount = 0
            albumList = ""
            for album in band["Albums"]:
                if albumCount != 0:
                    albumList += ", "
                albumCount += 1
                albumList += "\"" + album + "\""
            print "%s - %s - %i albums: %s" % (band["Name"], band["Genre"], albumCount, albumList)

main()