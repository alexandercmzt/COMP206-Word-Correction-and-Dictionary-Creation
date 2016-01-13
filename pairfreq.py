#Alexander Chatron-Michaud, 260611509

import sys, string, os.path, pickle

if len(sys.argv) != 2:
	print "sorry, please enter a valid text file as a command line argument!"
	exit()
if os.path.isfile(sys.argv[1]) != True:
	print "sorry, please enter a valid text file as a command line argument!"
	exit()
inputFile = open(sys.argv[1],'r')

inputText = inputFile.read()
inputText = inputText.lower()
inputText = inputText.replace("("," ")
inputText = inputText.replace(")"," ")
inputText = inputText.replace("]"," ")
inputText = inputText.replace("\""," ")
inputText = inputText.replace("["," ")
inputText = inputText.replace(","," ")
inputText = inputText.replace("."," ")
inputText = inputText.replace(":"," ")
inputText = inputText.replace(";"," ")
inputText = inputText.replace("'"," ")
inputText = inputText.replace("!"," ")
inputText = inputText.replace("\n", " ")
inputFile.close()


wordList = inputText.split()
wordPairs = {}
i = 0
k = len(wordList)-1
wordPairString = ""
while i < k :
	wordPairString = (wordList[i],wordList[i+1])
	if wordPairs.has_key(wordPairString) != 1:
		wordPairs[wordPairString] = 1
	else :
		wordPairs[wordPairString] = wordPairs[wordPairString] + 1
	i = i+1

pickle.dump(wordPairs, open("dictionary.pickle", "w"))

for key in wordPairs.keys():
	print "['" + str(key[0]) + "', '" + str(key[1]) + "'] " + str(wordPairs[key])



