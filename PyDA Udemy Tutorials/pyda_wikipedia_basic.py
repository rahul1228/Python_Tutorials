import wikipedia

while True:
	input = raw_input("Q?: ")
	wikipedia.set_lang("en")

	print wikipedia.summary(input, sentences=5) 
	# ^wikipedia.summary function takes user inputs and only shows 1st 5 sentences of article