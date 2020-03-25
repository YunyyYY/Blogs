from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import re


def luoxia():
	index = requests.get('https://www.luoxia.com/modu/')
	soup = BeautifulSoup(index.content, 'html.parser')
	mylist = soup.findAll("div", {"class": "book-list clearfix"})
	mylist = mylist[0]
	lis = mylist.find_all('a')
	title = []
	urls = []
	for a in lis:
    	urls.append(a.get('href'))
    	title.append(a.contents[0])
    
	for url in urls:
    	page = requests.get(url)
    	soup = BeautifulSoup(page.content, 'html.parser')
    	raw_ = soup.find(id='nr1')
    	break
    
	with open('modu.txt','w') as f:
    	for url in urls:
        	page = requests.get(url)
        	soup = BeautifulSoup(page.content, 'html.parser')
        	raw = soup.find(id='nr1')
            if not raw:
                continue
        	for p in raw.contents:
            	try:
                	if p.name == 'p':
                    	f.write(p.contents[0] + '\n')
            	except:
                	pass
        	f.write('\n\n')
        	break


def mitu():
	# parse menu page
	index = requests.get('https://www.m2m2.net/chapters_100365.html')
	soup = BeautifulSoup(index.content, 'html.parser')
	# parse chapter urls
	mylist = soup.findAll("ul", {"class": "dirlist three clearfix"})
	mylist = mylist[0]
	lis = mylist.find_all('a')
	title = []
	urls = []
	for a in lis:
    	urls.append(a.get('href'))
    	title.append(a.contents[0])
    # parse chapter and write to file
    with open('mhqz.txt','w') as f:
    	for url in urls:
        	page = requests.get(url)
        	soup = BeautifulSoup(page.content, 'html.parser')
        	raw_text = soup.find(id='chaptercontent')
        	for p in raw_text.contents:
            	try:
                	if p.name == 'p':
                    	f.write(p.contents[0] + '\n')
            	except:
                	pass
        	f.write('\n\n')
