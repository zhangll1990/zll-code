#!/usr/bin/env python

import random
import string
import requests
from bs4 import BeautifulSoup
import time

zone_number = []

def Id():
	A = string.join(random.sample('12345678',6)).replace(" ","")
	url = "http://www.360doc.com/content/12/0917/16/1888675_236595612.shtml"
	html = requests.get(url)
	html.encoding = 'utf-8'
	soup = BeautifulSoup(html.text,'lxml')
	#for info in soup.find_all(class_='MsoNormal'):
	#	zone_number.append('info.text')

	now = time.strftime('%Y')
	year =  random.randint(1948,int(now)-18)
	three = random.randint(1,12)
	if three < 10:
		month = '0' + str(three)
	else:
		month = three
	four = random.randint(1,31)
	if four < 10:
		day = '0' + str(four)
	else:
		day = four
	five = random.randint(1,9999)
	if five < 10:
	    five = '000' + str(five)
	    id =  five
	elif 10 < five < 100:
	    five = '00' + str(five)
	    id =  five
	elif 100 < five < 1000:
	    five = '0' + str(five)
	    id  =  five
	else:
	    id =  five
	IDcard = A + str(year) + str(month) + str(day) + str(five)
	print IDcard
Id()
