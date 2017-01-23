print "Enter a sentence to be snorkified:",
sentence_original = raw_input()
sentence_encrypted = sentence_original

sentence_encrypted = sentence_encrypted.replace('a', str(len(sentence_original)))
sentence_encrypted = sentence_encrypted.replace('e', str(len(sentence_original)+1))
sentence_encrypted = sentence_encrypted.replace('i', str(len(sentence_original)+2))
sentence_encrypted = sentence_encrypted.replace('o', str(len(sentence_original)+3))
sentence_encrypted = sentence_encrypted.replace('u', str(len(sentence_original)+4))

print "The encrypted sentence is %s" % sentence_encrypted
print "The decrypted sentence is %s" % sentence_original