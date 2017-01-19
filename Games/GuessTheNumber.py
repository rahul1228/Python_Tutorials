import random

def is_valid_num(s): # function checks if users guess is valid
	if s.isdigit() and 1 <= int(s) <= 100: # if users guess is a digit and if its between 1 and 100 using int(s) function. s.isdigit()
		return True # valid number
	else:
		return False # not valid number

def main():
	number = random.randint(1,100) # number gets random number using ranint() function from random lib.
	guessed_number = False # whether the user has guessed the number correctly aka game over.
	print "------------------Welcome to Number Guess------------------"
	guess = raw_input("Guess a number between 1 and 100: ") #asks user for input
	num_guesses = 0 # tracks number of guesses
	#----------Main Game Loop-------------------
	while not guessed_number: # while user hasn't guessed the # yet.
		if not is_valid_num(guess): #if users guess is not a valid number
			guess = raw_input("I won't count that one. A number between 1 and 100, ya bish: ") #asks user for a valid #
			continue # runs while loop from top again
		else:
			num_guesses += 1
			guess = int(guess) # use int() function to continue the while loop here bc, users inputs as a string

		if guess < number:
			guess = raw_input("Too low. Guess again: ")
		elif guess > number:
			guess = raw_input("Too high. Guess again: ")
		else:
			print "You got it in",num_guesses,"guesses!"
			guessed_number = True # user wins!


main()