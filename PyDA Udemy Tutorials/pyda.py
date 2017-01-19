import wolframalpha
import wikipedia

while True: #This is called a foreve loop bc no condition set to make it False
	input = raw_input("Q?: ")

	# Below code is a try/except loop
	# it first executes the try block code for wolfram 
	# if that dont work/causes an error then...
	# it does the exception block code
	try:
		# Wolfram alpha
		app_id = "XGUKWK-AU3YR5AVAJ"
		client = wolframalpha.Client(app_id) #create client from app_id
		res = client.query(input) #user question put into query function from wolfram
		answer = next(res.results).text #displays results as text. next function keeps running query until text data is found for user question
		print answer
	except:
		# Wikipedia
		print wikipedia.summary(input, sentences=5) 
		# ^wikipedia.summary function takes user inputs and only shows 1st 5 sentences of article
