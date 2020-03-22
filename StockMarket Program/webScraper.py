# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:45:18 2020

@author: Ralph
"""
import time
import bs4
import requests
from bs4 import BeautifulSoup

starttime=time.time()
strikePrice = 0
input_strike = '160.00'
counter = -1


def getPrice():
    
    r = requests.get('https://finance.yahoo.com/quote/SPY?p=SPY')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price
#    r.close()
    
def getStrike():
    strikePrice = 0
    counter = -1
    while strikePrice!=input_strike:
        counter = counter + 1
        r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY')
        soup = bs4.BeautifulSoup(r.text,"lxml")
        strikePrice = soup.find_all('a',{'class': 'C($linkColor) Fz(s)'})[counter].text
    else:
         r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY')
         soup = bs4.BeautifulSoup(r.text,"lxml")
         optionPrice = soup.find_all('td',{'class': 'data-col3 Ta(end) Pstart(7px)'})[counter].text
         return strikePrice,optionPrice

while True:
    a, b = getStrike()
    print ('The current SPY price is: ' + str(getPrice()))
    print ('The current SPY strike price is: ' + str(getStrike()))
    print ('The current SPY option price for this strike is: ' + str(getStrike()))    
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))