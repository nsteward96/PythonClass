file = open('Text.txt', 'r')
discarded = []

for line in file:
    words = line.split(' ')
    for word in words:
        temp = word.replace(',', '')
        temp = temp.replace('.', '')
        if len(word) == 4:
            discarded.append(word)
        else: 
            print word + " ",
       
print "\n\nDiscarded words: %s" % discarded