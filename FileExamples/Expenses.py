import Epic

kmWeekday = Epic.userInt("How many km did you travel on a weekday?")
miWeekday = Epic.kmToMi(kmWeekday)

kmWeekend = Epic.userInt("How many km did you travel on a weekend?")
miWeekend = Epic.kmToMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13
dollarsWeekend = miWeekend * 0.24

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend
print "Total $%.2f" % (dollarsWeekday + dollarsWeekend)