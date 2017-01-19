from six.moves import urllib
import io

def get_robots_txt(url):
	# Url check
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	# Below Opens url/robots.txt webpage then...
	# ...stores what it opens into second parameter var data
	req = urllib.request.urlopen(path + "robots.txt", data=None)
	# Encodes whatever is stored in data var properly
	# data = io.TextIOWrapper(req, encoding='utf-8')
