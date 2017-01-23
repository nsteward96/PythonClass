print "How many malcorps did you find on planet Exflon?",
malcorps_exflon = raw_input()
print "How many malcorps did you find on planet Mobiles?",
malcorps_mobiles = raw_input()
print "How many malcorps did you find on planet Monsantoes?",
malcorps_monsantoes = raw_input()

total = int(malcorps_exflon) + int(malcorps_mobiles) + int(malcorps_monsantoes)
average = total/3.0

print "You found %i malcorps!" % total
print "The average malcorps per planet is %.2f." % average