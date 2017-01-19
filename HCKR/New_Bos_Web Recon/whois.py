import os

def get_whois(url):
	command = 'whois ' + url # Whois command
	process = os.popen(command) # opens command promts, runs command
	results = str(process.read()) # stores results as string in results
	return results