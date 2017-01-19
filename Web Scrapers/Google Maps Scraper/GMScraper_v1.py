import urllib
import mechanize
from bs4 import BeautifulSoup
import re

def getGoogleMapsLinks(searchTerm):
	searchTerm = searchTerm.replace(" ", +) # replace user query spaces with plus bc thats how google search url works
	
