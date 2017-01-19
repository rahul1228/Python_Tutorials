'''
+ Links will be in the queue list.
+ One link will be picked from list
+ It will connect to that page
+ Once connected it will grab all the html from page and put it into link_finder
+ link_finder will then parse the html for links 
+ Then it will add those links to the queue list
+ All crawled pages will be taken off queue list and put into crawled list
+ All spiders share the same queue and crawled files
+ Sets are stored in the ram and not in the hard drive.
+ Files are stored in the HD.
AKA THIS PROGRAM IS MULTI-THREADED
'''
from urllib import *
from urllib import urlopen
from urllib2 import *
from link_finder import LinkFinder
from general import *


class Spider:

	# Class variables are shared among all instances of Spider
	# If these were in the init function they would be unique to each spider and not shared
	# But the objective is to have all spiders share the queue & crawled files
	# So class vars are used
	# Now in the init function you will see Spider. vars and not self. vars
	project_name = ''
	base_url = ''
	domain_name =''
	queue_file = ''  
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name # What user passes
		Spider.base_url = base_url # What user passes
		Spider.domain_name = domain_name # What user passes
		Spider.queue_file = Spider.project_name + '/queue.txt'
		Spider.crawled_file = Spider.project_name + '/crawled.txt'
		self.boot()
		self.crawled_page('First spider', Spider.base_url) 

	# Creates Spider
	# static methods dont need self in params bc its for individual Spider
	# Instead we use the indicator: Spider.something
	# It means that this method/function could be outside of this class
	# This is just Python proper convention
	# Dont have to use the convention. Can do regular way with self param as well
	@staticmethod 
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file) # adds queue file to queue set
		Spider.crawled =file_to_set(Spider.crawled_file) # adds crawled file to crawled set


	# Crawled page function
	# adds links to queue
	# removes crawled url from queue set then adds into crawled set
	# Then it updates the files 
	@staticmethod
	def crawled_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print thread_name + " now crawling: " + page_url
			print 'Queue: ' + str(len(Spider.queue)) + " | Crawled: " + str(len(Spider.crawled))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url) # removes url from queue set
			Spider.crawled.add(page_url) # adds url to crawled set
			Spider.update_files()


	@staticmethod
	def gather_links(page_url):
		html_string = '' # empty string
		try:
			response = urlopen(page_url) # open url store in response
			if 'text/html; charset=UTF-8' in response.getheader('Content-Type'): # if response is text/html
				html_bytes = response.read() # read response store in html_bytes
				html_string = html_bytes.decode('utf-8') # decode()function from urllib turns bytes to html string utf encoded
			finder = LinkFinder(Spider.base_url, page_url) # LinkFinder Object Initialization/Instance of class LinkFinder
			finder.feed(html_string) # .feed() function from HTMLParser, from LinkFinder object called finder it parses the html
		except:
			print 'Error: Unable to crawl page'
			return set() # return empty set for error handlin purposes
			
		return finder.page_links() # function from LinkFinder


	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue: 
				continue # dont add, go to next url/continue for loop
			if url in Spider.crawled: 
				continue # dont add, go to next url/continue for loop
			if Spider.domain_name not in url: 
				# this makes sure it only crawls links connected to the 1st website.
				# So if it sees google.com link on my website it will not add to queue list
				continue
			Spider.queue.add(url)

	
	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)

