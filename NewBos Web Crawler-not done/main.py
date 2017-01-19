"""**************************************************************************************
-------------------------------------WEBCRAWLER---------------------------------------
How this Program works: You put in a url to start crawling from, say WSJ Homepage.
It will open that page and then strip all the links from that page and add
those links to the queue file. It will then crawl each of those links in the queue file
and repeat the process. Till it crawls all links connected to the base url.
The program checks to see if it has crawled all links by adding the urls to the
crawled file. CHECK spider.py FOR MORE INFO

+ Data is stored in sets(like a list but more like tuple) then put into the files a bunch at a time.
+ Sets are stored in the ram and not in the hard drive.
This way the program is faster.
Rather than the normal way which is store the data straight into the files one by one one after the other.
Which is the slower way. AKA THIS PROGRAM IS MULTI-THREADED. 
+ EACH THREAD/Spider can do a different job but unlike a regular program each thread can work at the
same time

+ All spiders share the same queue and crawled files
***************************************************************************************"""
import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *

# Constant variables are vars that never change in the running of your program
# They are noted by all caps
PROJECT_NAME = 'newbos'
HOMEPAGE ='https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8 # The number of threads you can run depends on operating system

queue = Queue() # Queue function from queue package/library. Used for threading. Thread Queue

# Spider object/Instance of Spider class
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME) 



