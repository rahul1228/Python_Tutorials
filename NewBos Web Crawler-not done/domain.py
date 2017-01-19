from urllib import *
from urlparse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.') #splits url on . so makes it into list item
		return results[-2] + '.' + results[-1] # return second to last and last item in results list
	except:
		return ''

# Get sub domain name from full url (name.example.com)
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc # Built in urlparse function gets url net location
	except:
		return '' 