import random

def get_word():
	words = ["Goku","Krillin","Cell","Buu","Gohan","Vageta","Trunks","Bulma","Yamcha","Frieza"]
	return random.choice(words).upper() #random.choice() = built in function in random lib that randomly chooses a index/element from list/var passed in. It picks an element in a sequence.

def check(word,guesses,guess):
	status = "" #***status var = the word we are going to return to the user
	matches = 0

	for letter in word: #loop thru all letters/characters in our answer word
		if letter in guesses: #if the letter from answer word is one of the user's guesses
			status += letter #show that letter
		else:
			status += "*" #otherwise show a *

		if letter == guess: #if letter from the answer word matches the user's guess
			matches += 1

	if matches > 1: #if there is more than one match
		print "Yes! The word contains", matches,"", + guess + "" + "s" #EX: Yes! The word contains 2 A s
	elif matches == 1:
		print "Yes The word conatins the letter: " +guess + "" #EX: Yes! The word contains the letter A
	else: #if no matches
		print "Sorry. The word does not contain the letter: " + guess + ""

	return status

def main():
	word = get_word()
	guesses = []
	guessed = False
	print "------------------Welcome to Word Guess------------------"
	print "The word contains",len(word),"letters."
	#------Main Game Loop-----
	while not guessed: # while guessed is false
		text = 'Please enter one letter or a {}-letter word: '.format(len(word)) #len(word) will replace the curly brackets in the string. EX: Please enter one letter or a 9 letter word.
		guess = raw_input(text) # gets input from user and stores in guess
		guess = guess.upper()

		if guess in guesses: #does guess the user just enetered exist in guesses list. Whole word guess only
			print "You already guessed" + guess + ""
		elif len(guess) == len(word): # if user input guess length is the same number as the answer word
			guesses.append(guess)
			if guess == word: #and if that user guess also happens to be the exact answer word  then
				guessed = True
			else:
				print "Sorry, that is incorrect."
		elif len(guess) == 1: # if user inputs/enters only 1 character
			guesses.append(guess)
			result = check(word,guesses,guess)
			if result == word:
				guessed = True
			else:
				print result
		else: # if user didnt enter/input anything
			print "Invalid entry!"

	print "Yes, the word is", word + "! You got it in", len(guesses), "tries."



main()