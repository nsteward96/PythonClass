print "What is your name?"
name = raw_input()
print "%s, your name is %s characters long." % (name, len(name))

s1 = "Python is boring!"
s2 = s1.replace('boring', 'awesome')

print "%s, %s" % (s1, s2)

print s2[3] # => "h"

print "Python" in s1  # Will print "true" if 'Python' is found within s1. Else, prints false.

print "Please enter a word:",
word = raw_input()
print "Please enter a number:",
num = raw_input()
print "I am the great repeater -- watch this! %s" % (word * int(num))