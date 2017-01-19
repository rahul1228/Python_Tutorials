import wolframalpha

while True:
	pass
	input = raw_input("Question: ")
	app_id = "XGUKWK-AU3YR5AVAJ"
	client = wolframalpha.Client(app_id) #create client

	res = client.query(input) #user question put into query function from wolfram
	answer = next(res.results).text #displays results as text. 

	print answer