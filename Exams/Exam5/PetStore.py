################################################################################
#   PetStore
#   - Written by Nate Steward 4-16-17
#   - Search for an item in our petstore. We have food, furniture, and toys!
#   - Search by category or by keyword. We will give you a list of items
#       that match your search.
################################################################################
import Epic
import json

################################################################################
#   main()
#   - No arguments, returns nothing.
#   - Runs all of the main functions of the program.
#   - Stores json in storeContents.
#   - Asks user which type of search they would like to make - category,
#       or keyword.
#   - Asks user to enter their search.
#   - Searches the storeContents json for products that match the search.
################################################################################
def main():
    storeContents = processJson()
    userSearchType = str.upper(Epic.userString("Search by category (c) or keyword (k)? "))
    userSearch = processRequest(str.capitalize(userSearchType))
    search(userSearch, userSearchType, storeContents)

################################################################################
#   processJson()
#   - No arguments, returns storeResults (the processed json)
#   - Opens the PetStore.json file and processes it into text we can work with.
################################################################################
def processJson():
    jsonText = ""
    file = open('PetStore.json')
    for line in file:
        line = line.strip()
        jsonText = jsonText + line
    storeResults = json.loads(jsonText)
    return storeResults

################################################################################
#   processRequest(userSearchType)
#   - Takes a String userSearchType as an argument, returns userSearch (user's 
#       keywords)
#   - Allows user to enter in key words for their search.
################################################################################
def processRequest(userSearchType):
    userSearch = ""
    if userSearchType == "C":
        userSearch = Epic.userString("Enter a category: ")
    elif userSearchType == "K":
        userSearch = Epic.userString("Enter a keyword: ")
    return userSearch

################################################################################
#   search(userSearch, userSearchType, json)
#   - Takes arguments String userSearch, String userSearchType, and Dictionary
#       json.
#   - Searches the json for matches to the user's search keywords for its
#       search type.
#   - Prints the total search results.
################################################################################
def search(userSearch, userSearchType, json):
    finalResults = ""
    if userSearchType == "C":
        for item in json:
            if unicode.upper(item["Category"]) == str.upper(userSearch):
                finalResults = finalResults + format("%s - %s\n" % (str(item["Product"]), str(item["Price"])))
    elif userSearchType == "K":
        for item in json:
            if str.upper(userSearch) in str(unicode.upper(item["Product"])):
                finalResults = finalResults + format("%s - %s\n" % (str(item["Product"]), str(item["Price"])))
    print finalResults

################################################################################
#   Run the main program
################################################################################
main()