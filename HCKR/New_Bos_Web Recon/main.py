from general import*
from domain_name import*
from ip_address import*
from nmap import*
from robots_txt import*
from whois import*

# Creating Root Directory/folder
ROOT_DIR = 'companies' #Constant
create_dir(ROOT_DIR)

# Below gather_info function calls alot of functions from our other scripts
# param name = company name aka google
# param url is url we wanna gather info on
def gather_info(name, url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(url)
	n_map = get_nmap('-F', ip_address)
	robo_txt = get_robots_txt(url)
	who_is = get_whois(domain_name)
	create_report(name, url, domain_name, n_map, robo_txt, who_is)

def create_report(name, full_url, domain_name, n_map, robo_txt, who_is):
	# directory where report will be stored. example: companies/google
	project_dir = ROOT_DIR + '/' + name 
	# Creates directory
	create_dir(project_dir)
	# Write file function param 1)path param 2)data to write to
	write_file(project_dir + '/full_url.txt', full_url)
	write_file(project_dir + '/domain_name.txt', domain_name)
	write_file(project_dir + '/nmap.txt', n_map)
	write_file(project_dir + '/robots.txt', robo_txt)
	write_file(project_dir + '/whois.txt', who_is)

def main():
	name = raw_input("What website company do you want to scan: ")
	url = raw_input("Please input the full url for its wesbite: ")
	gather_info(name,url)

main()