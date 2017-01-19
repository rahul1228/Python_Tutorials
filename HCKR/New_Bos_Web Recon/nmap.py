import os

def get_nmap(options, ip):
	command = 'nmap ' + options + " " + ip # Nmap command
	process = os.popen(command) # Opens cmd prompt and runs command
	results = str(process.read()) # Puts results in string format stores in results 
	return results