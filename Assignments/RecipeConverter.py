# Nathan Steward
# Recipe Converter for Python Class 1-22-17

import math

# While the user hasn't finished the input process without making a mistake
while True:
    # Inputting process, user inputs original recipe
    try:
        print "-- Original Recipe --"
        print "Enter the amount of Flour (cups):",
        flour_cups = float(raw_input())
        print "Enter the amount of water (cups):",
        water_cups = float(raw_input())
        print "Enter the amount of salt (teaspoons):",
        salt_teaspoons = float(raw_input())
        print "Enter the amount of yeast (teaspoons):",
        yeast_teaspoons = float(raw_input())
        print "Enter the loaf adjustment factor (e.g. 2.0 double the size):",
        loaf_adjustment_factor = float(raw_input())
    # If an error occurs, the user must start over.
    except ValueError:
        print "A valid number or float was not entered. Let's take it from the top..."
        print
    except Exception:
        print "Oh no, something bad happened and I don't know what it was! Maybe we just need to go back..."
        print
    # If the user doesn't mess up, they move on to the next section.
    else:
        break

print
    
# User gets the recipe back in the desired amount, e.g. 2 times the original amounts entered.
print "-- Modified Recipe --"
print "BreadFlour: %.2f cups." % float(flour_cups*int(loaf_adjustment_factor))
print "Water: %.2f cups." % float(water_cups*int(loaf_adjustment_factor))
print "Salt: %.2f teaspoons." % float(salt_teaspoons*int(loaf_adjustment_factor))
print "Yeast: %.2f teaspoons." % float(yeast_teaspoons*int(loaf_adjustment_factor))
print "Happy Baking!"
    
print
    
# Variables for grams per unit of measurement for ingredient
grams_per_cup_flour = 120.0
grams_per_cup_water = 237.0
grams_per_teaspoon_salt = 5.0
grams_per_teaspoon_yeast = 3.0
    
# User gets the recipe back in the desired amount, using grams instead of cups.
print "-- Modified Recipe in Grams --"
print "BreadFlour: %.2f g." % float(math.floor(flour_cups * grams_per_cup_flour) * int(loaf_adjustment_factor))
print "Water: %.2f g." % float(math.floor(water_cups * grams_per_cup_water) * int(loaf_adjustment_factor))
print "Salt: %.2f g." % float(math.floor(salt_teaspoons * grams_per_teaspoon_salt) * int(loaf_adjustment_factor))
print "Yeast: %.2f g." % float(math.floor(yeast_teaspoons * grams_per_teaspoon_yeast) * int(loaf_adjustment_factor))
print "Happy Baking!"