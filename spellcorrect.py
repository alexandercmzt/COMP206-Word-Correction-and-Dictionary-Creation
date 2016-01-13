#Alexander Chatron-Michaud, 260611509

import pickle, sys, os, string, difflib

if len(sys.argv) != 2:
	print "sorry, please enter a valid pickle/dictionary file as a command line argument! (The default pickle created by pairfreq.py is dictionary.pickle)"
	exit()
if os.path.isfile(sys.argv[1]) != True:
	print "sorry, please enter a valid pickle/dictionary file as a command line argument! (The default pickle created by pairfreq.py is dictionary.pickle)"
	exit()
dictionary = pickle.load(open(sys.argv[1], "r"))
wordList = []
for key in dictionary.keys() :
	if key[0] not in wordList :
		wordList.append(key[0])
	if key[1] not in wordList :
		wordList.append(key[1])

print "ENTER q IN STDIN TO END THE PROGRAM"
while True:
	inputString = raw_input("Enter a pair of words: ")
	inputString = inputString.lower()
	twoWords = inputString.split()
	correct = 0
	if len(twoWords)==1 and twoWords[0] == "q":
		print "Ended Program."
		exit()
	if len(twoWords) != 2 :
		print "Incorrect format, enter a pair of words"
		continue
	for key in dictionary.keys() :
		if twoWords[0] == key[0] or twoWords[0] == key[1]:
			print "The first word is spelled correctly!"
			correct = 1
			break
	if correct == 1:
		continue
	else :
		fixList = difflib.get_close_matches(twoWords[0], wordList, 10)
		fixPairs = []
		for fix in fixList:
			for key in dictionary.keys():
				if key[0] == fix :
					fixPairs.append(key)
		decisionStrength = -1
		for answers in fixPairs :
			if answers[1] == twoWords[1] :
				if dictionary[answers] > decisionStrength :
					decisionStrength = dictionary[answers]
					decision = answers
		if decisionStrength == -1 and not fixList :
			print "The program could not correct this as the dictionary does not contain any similar words"
			continue
		if decisionStrength == -1 :
			print fixList[0] + " " + twoWords[1]
			print "The above correction was weak, as it could not find word pairs with the second word in the dictionary. Instead a similar word that exists in the dictionary has been suggested, however it may not be correct."
			continue
		print decision[0] + " " + decision[1]


