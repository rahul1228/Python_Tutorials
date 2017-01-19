from distutils.core import setup
import py2exe

setup(console=['gmail.py'], 
	options={'py2exe': {
				'packages': ['smtplib']
	}})