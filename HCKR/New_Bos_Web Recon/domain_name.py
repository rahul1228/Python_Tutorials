from tld import get_tld

# Strips top level domain name from full url if your list contains full urls
# So https://www.google.com gets returned like, google.com
def get_domain_name(url):
	domain_name = get_tld(url)
	return domain_name

