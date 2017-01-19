from threading import Thread
import urllib
import re #regular expressions library used for scraping
import MySQLdb

# urls = "http://google.com http://cnn.com http://wikipedia.com http://yahoo.com".split()
# ^ by using split function on a string it turns it into an array/list
#Multi-Threading is the ability of a program or an operating system process to manage its use by more than one user at a time and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer. 
#The reason we are defining a function is bc we need seperate memory allocation for each thread

conn = MySQLdb.connect(host="",user="",passwd="",db="")

def th(ur):
	baseurl = "http://www.nasdaq.com/symbol/"+ur
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+)</div>'# re use step1) give it html tag u want it to look for
	pattern = re.compile(regex)# re use step2) compile it so comp can understand
	htmltext = urllib.urlopen(baseurl).read()# when u open and read a file it turns it into a string
	results = re.findall(pattern,htmltext) # re use step3) use findall function to get results
	print str(ur) + " " +"Last Price: " + str(results[0]) + "\n" #we convert the vars to strings bc when threading and printing the data it can get jumbled otherwise/ print not in order if we used: print ur,results
	# ^ we use results[0] bc otherwise it willprint the list/array brackets too
	#^ in the results var the price is stored as element 0

symbolsfile = open("symbols.txt").read() # when u open and read a file it turns it into a string
symbolsfile = symbolsfile.split()

threadlist = []

for s in symbolsfile: # here we start all the threads
	t = Thread(target = th, args =(s,)) #t hread function takes a target function & args for the target function
	t.start()
	threadlist.append(t)

for b in threadlist: # here we join all the threads back to main memory
	b.join()


