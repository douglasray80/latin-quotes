#!/usr/bin/python

import urllib2
import re
from bs4 import BeautifulSoup

page = 'https://best-quotations.com/latin-quotes.php?page='
count = 1

with open('quotes.json', 'a+') as txt_file:
    print('Opening file...')
    txt_file.write('[\n')
    while count < 7:
        print('Scraping page ' + str(count) + '...')
        url = urllib2.urlopen(page + str(count))
        soup = BeautifulSoup(url, 'html.parser') 
        quotes = soup.find_all(class_='quote')
    
        for quote in quotes:
            text = quote.b.string.encode('utf-8')
            translation = quote.find(class_='expln').string.encode('utf-8')
            if quote.find(class_='auth0'):
                author = quote.find(class_='auth0').a.string.encode('utf-8')
            else:
                author = quote.find(class_='auth2').string.encode('utf-8')
            
            txt_file.write('{\n' + '\t"quote": "' + text + '",\n' + '\t"translation": "' + translation + '",\n' + '\t"author": "' + author + '",\n' + '},\n')
            
        print('Finished scraping page ' + str(count))
        count += 1

    txt_file.write(']')
    print('Finished!')