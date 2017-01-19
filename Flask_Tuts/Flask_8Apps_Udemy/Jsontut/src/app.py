import requests
from bs4 import BeautifulSoup

r = requests.get("https://http://www.johnlewis.com/original-penguin-peached-jersey-cotton-t-shirt/p3129537?colour=Deep%20Lake%20Heather")
content = r.content # content from requests pulls all the websites contents/html
soup = BeautifulSoup(content) # runs BS function to parse the content var
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
print(element.text.strip()) # .text function = from BS to convert into text