from HTMLParser import HTMLParser
from urllib import *
from urlparse import urlparse

class LinkFinder(HTMLParser):# inherits from HTMLParser

	# Class/Object Initialization function. Whats called when an object instance of this class is created.
	# It contains all of the instance variables
	def __init__(self, base_url, page_url):
		super().__init__() # super class initialization method. 
		self.base_url = base_url # What user passes
		self.page_url = page_url # What user passes
		self.links = set() # empty set thats going to be used for the links

	# Parses Links and adds to links set
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs: # for loops can store in tuples too!
				if attribute == 'href':
					# Parses  href attribute. 
					#Pulls value from it, and joins it to base_url if the value didnt have it.
					url = urlparse.urljoin(self.base_url, value)
					# Adds url to links set
					self.links.add(url)

	# Returns links set's items
	def page_links(self): 
		return self.links

	# Built in Error handling function
	def error(self,message): 
		pass



