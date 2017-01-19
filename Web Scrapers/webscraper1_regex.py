import urllib #package/library that allows us to make network requests
import re #regular expressions library/package

urls = ["https://google.com","https://nytimes.com","http://cnn.com"]

i = 0

regex = '<title>(.+?)</title>' 
pattern = re.compile(regex) #converts regex string into what can be determined by re library

while i < len(urls):

	htmlfile = urllib.urlopen(urls[i]) #runs urlopen function from urllib package...
	#^ ...for every url in list urls and stores it in variable htmlfile

	htmltext = htmlfile.read() #read function is from urllib
	#^displays html text from htmlfile variable using read function

	titles = re.findall(pattern, htmltext)
        #^findall function from the re library gets anything between title tags in htmml scripts
        #^parameters, pattern = what findall should look for & htmltext = from where its looking from
	print titles

	i += 1




