import os

# Gets IP for url using command line tool, host
def get_ip_address(url):
	command = 'host ' + url # cmd command to look up an IP is: host google.com
	process = os.popen(command) # Opens cmd prompt and runs command
	results = str(process.read()) # Puts results in string format 
	marker = results.find('has address') + 12 # Finds part of string in full string 
	# Below Returns results but from marker to end of string/results
	# .splitlines() function is added on to ensure only 1st...
	# ...IP address is taken if website has multiple IPs
	# It does the by splitting results into seperate lines and takes 1st line.
	return results[marker:]

	