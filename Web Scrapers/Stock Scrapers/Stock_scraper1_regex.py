import urllib #package/library that allows us to make network requests
import re #regular expressions library/package

symbolfile = open("symbols.txt") #opens .txt file containing symbols stores in variable symbolfile
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split() #.split("/n")=buil-in python function that splits string files so comp can read 1 by one in loop. in this case it splits the invisible /n in the txt file denoting new line.

pricelist= []

i = 0

while i < len(newsymbolslist):
	url = "http://www.nasdaq.com/symbol/" + newsymbolslist[i]
	
	htmlfile = urllib.urlopen(url) #runs urlopen function from urllib package...
	#^ ...for every url in list urls and stores it in variable htmlfile

	htmltext = htmlfile.read() #read function is from urllib
	#^displays html text from htmlfile variable using read function

	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+)</div>' #(.+?) means that the part of the where it will scrape the info from.
	pattern = re.compile(regex) #converts regex string into what can be determined by re library

	price = re.findall(pattern,htmltext)
	#^findall function from the re library gets anything between title tags in htmml scripts
	#^parameters, pattern = what findall should look for & htmltext = from where its looking from
	
	pricelist.append(price)
	print newsymbolslist[i].upper(),"Last Price: ",price 	
	i += 1





