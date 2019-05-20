#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

## this script will scrape the text, translation, and author from the first div with the class of quote
page = 'https://best-quotations.com/latin-quotes.php'

url = urllib2.urlopen(page)
soup = BeautifulSoup(url, 'html.parser')
quote = soup.find(class_='quote')

with open("example.json", "a+") as myfile:
	text = quote.b.string.encode('utf-8')
	translation = quote.find(class_='expln').string.encode('utf-8')
	author = quote.find(class_='auth0').find('a').string.encode('utf-8')
	
	# print(author)
	myfile.write('{\n' + '\t"quote": "' + text + '",\n' + '\t"translation": "' + translation + '",\n' + '\t"author": "' + author + '",\n' + '},')