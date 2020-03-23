# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:01:44 2020

@author: Ralph
"""
import time
import bs4
import requests
from bs4 import BeautifulSoup

strikePrice = 0
input_strike = '160.00'
counter = -1
## Find Strike Price 
while strikePrice!=input_strike:
    counter = counter + 1
    r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    strikePrice = soup.find_all('a',{'class': 'C($linkColor) Fz(s)'})[counter].text
else:
    print ('')
    print (strikePrice)
    print (counter)

#find Option last value

    r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    optionPrice = soup.find_all('td',{'class': 'data-col3 Ta(end) Pstart(7px)'})[counter].text
    percentCng = soup.find_all('td',{'class': 'data-col7 Ta(end) Pstart(7px)'})[counter].find('span').text
    print (optionPrice)
    print (percentCng)