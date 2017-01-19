import urllib
import re
import json

symbolfile = open("symbols.txt") #opens .txt file containing symbols stores in variable symbolfile
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split() #.split("\n")=buil-in python function that splits string files so comp can read 1 by one in loop. in this case it splits  on the new line "\n" in the txt file denoting new line.


i = 0

while i < len(newsymbolslist):
	url = "http://www.bloomberg.com/markets/api/security/basic/" + newsymbolslist[i] + "%3AUS?locale=en" 
	
	htmlfile = urllib.urlopen(url) #runs urlopen function from urllib package...
	#^ ...for every url in list urls and stores it in variable htmlfile

	data = json.load(htmlfile) #json.load function is from json library converts html file to json readable so you can pull shit

	print data["id"],"Last Price: ",data["price"],"Volume: ",data["volume"] #the data is stored like an array so u print the key of the value u want it to print
	i += 1


for symbol in newsymbolslist:
	myfile = open(symbol + ".txt", "w+")
	myfile.close()

	url = "http://www.bloomberg.com/markets/api/bulk-time-series/price/" + symbol + "%3AUS?timeFrame=1_DAY" 
	
	htmlfile = urllib.urlopen(url) #runs urlopen function from urllib package...
		#^ ...for every url in list urls and stores it in variable htmlfile

	data = json.load(htmlfile) #json.load function is from json library converts html file to json readable so you can pull shit

	datapoints = data[0]["price"] #pulling price ket data from file

	myfile = open(symbol + ".txt", "a")

	for point in datapoints:
		myfile.write(str(symbol+","+str(point["dateTime"])+","+str(point["value"])+"\n")) #"\n" = new line . dateTime & value are the dict keys data from file

	myfile.close()


#http://www.bloomberg.com/markets/api/security/basic/AAPL%3AUS?locale=en
#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL%3AUS?timeFrame=1_DAY
#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL%3AUS?timeFrame=1_DAY   <----daily chart prices