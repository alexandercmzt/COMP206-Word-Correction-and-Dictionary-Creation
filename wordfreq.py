#Alexander Chatron-Michaud, 260611509

import sys, string, os.path

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



textDictionary = {}
for word in inputText.split():
	if textDictionary.has_key(word) != 1:
		textDictionary[word] = 1
	else:
		textDictionary[word] = textDictionary[word] + 1

for key in textDictionary.keys():
	print key + " " + str(textDictionary[key])
