################################################################################
#   Weather - Written by Nate Steward
#   - Enter in a location and a preference of Fahrenheit or Celsius for temperature.
#   - Get back information on the weather for that location.
################################################################################

import Epic
import json
import urllib2

################################################################################
#   main() 
#   - No arguments, returns nothing
#   - Runs the weather program.
################################################################################
def main():
    running = True
    while running:
        weather = False
        while weather == False:
            url = getUrl()
            weather = getJson(url)
        tempType = getTempType()
        printWeather(weather, tempType)
        running = Epic.promptUserRunAgain("\nWant to check another location? (y/n) ")
    print "\nEnjoy the good weather while it lasts!"

################################################################################
#   getUrl()
#   - No arguments, returns a complete URL for the weather API.
#   - Asks user for the location they want weather information on.
#   - Formats the URL and returns it as a string.
################################################################################
def getUrl():
    url = "https://api.apixu.com/v1/current.json?key=643ef4b2a5ba4fab97e151415163103"
    location = Epic.userString("\nPlease enter a zipcode or city name: ").replace(" ", "_")
    url = url + "&q=%s" % location
    return url

################################################################################
#   getJson(url)
#   - Takes the URL string from getUrl as an argument, returns JSON weather info.
#   - Attempts to retrieve JSON information using the weather API.
#   - Checks for errors using the urllib2 library and a default error message.
################################################################################
def getJson(url):
    try:
        jsonTxt = urllib2.urlopen(url).read()
        weather = json.loads(jsonTxt)
        return weather
    except urllib2.HTTPError:
        print "There was an issue getting weather data for the location specified. Please enter a valid location."
        return False
    except:
        print "An unknown error occurred. Try typing in your location again."
        return False

################################################################################
#   getTempType()
#   - No arguments, returns the user's preferred temperature type as a
#       one-character string.
#   - Asks user for their preferred temperature type: Fahrenheit or Celsius.
################################################################################
def getTempType():
    tempType = Epic.user2OptionsString("Would you like Fahrenheit (F) or Celsius (C) temperatures?", "F", "C")
    return tempType

################################################################################
#   printWeather(weather, tempType)
#   - Takes weather (the weather JSON) and tempType (user's preference of F or C)
#       as arguments, returns nothing
#   - Prints the weather information for the user's specified area.
################################################################################
def printWeather(weather, tempType):
    print "\nHere is the weather for %s, %s." % (weather["location"]["name"], weather["location"]["region"])
    if tempType == "C":
        print "%s and %s degrees (C)." % (weather["current"]["condition"]["text"], weather["current"]["temp_c"])
    else:
        print "%s and %s degrees (F)." % (weather["current"]["condition"]["text"], weather["current"]["temp_f"])
    if tempType == "C":
        print "It actually feels like %s degrees (C)." % weather["current"]["feelslike_c"]
    else:
        print "It actually feels like %s degrees (F)." % weather["current"]["feelslike_f"]

################################################################################
#   Run the main program!
################################################################################
main()