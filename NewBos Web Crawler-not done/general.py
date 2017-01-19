"""**************************************************************************************
-------------------------------------WEBCRAWLER---------------------------------------
How this Program works: You put in a url to start crawling from, say WSJ Homepage.
It will open that page and then strip all the links from that page and add
those links to the queue file. It will then crawl each of those links in the queue file
and repeat the process. Till it crawls all links connected to the base url.
The program checks to see if it has crawled all links by adding the urls to the
crawled file. 

++Set:
Data is stored in sets (like a list but more like tuple) then put into the files a bunch at a time.
This way the program is faster.And safe b/c the data is saved rather than lost if program freezes/shutsdown/or has an error.
Rather than the normal way which is store the data straight into the files one by one one after the other.
Which is the slower way. Sets are stored in the ram and not in the hard drive.
+ All spiders share the same queue and crawled files
AKA THIS PROGRAM IS MULTI-THREADED

++With:
with keyword is used when working with unmanaged resources (like file streams)...
...to ensure that a resource is "cleaned up" when the code that uses it finishes running,..
...even if exceptions are thrown. It provides 'syntactic sugar' for try/finally blocks.
***************************************************************************************"""

import os

# Create project directories
# Each website you crawl = a seperate project (folder)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print "Creating directory for" + directory + "..."
		os.makedirs(directory)


# Create Queue and Crawled text files (if not created)
# Queue file will be text list of websites to crawl
# To keep track of what pages have already been crawled so process isnt repeated.
# Param base_url = the 1st page of the website, a starting point for this web crawler to start
def create_data_files(project_name,base_url):
	queue = project_name + '/queue.txt' # Queue file path var
	crawled = project_name + '/crawled.txt' # Crawled file path var
	if not os.path.isfile(queue): # If no que file
		write_file(queue,base_url) # Creates que file with base url as first wesbite in que
	if not os.path.isfile(crawled):
		write_file(crawled, '') # Creates blank crawled file bc if it hasn't been created b4 then we havent crawled shit


# Creates a new text file at path specified with data sgiven in params
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


# Add/Append data onto an existing file
def append_to_file(path,data):
	with open(path,'a') as file: # 'a'= append , file = var its stored in
		file.write(data + '\n')


# Delete the contents of a file
# Does this by creating a new file with the same name aka overwriting
def delete_file_contents(path):
	with open(path, 'w'):
		pass


# Read a file and convert each line to item in a set
def file_to_set(file_name):
	results = set()
	with open(file_name, "rt") as f: # rt= read text file
		for line in f:
			results.add(line.replace('\n', ''))
		return results


# Iterate through a set, each set item will be a new line in the text file
# Param sets holds the set, param file holds a filepath
def set_to_file(sets, file):
	delete_file_contents(file) # Makes sure file is clear for new data from the set
	for link in sorted(sets):
		append_to_file(file,link)

