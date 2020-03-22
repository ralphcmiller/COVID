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


def getPrice():
    
    r = requests.get('https://finance.yahoo.com/quote/SPY?p=SPY')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price
#    r.close()
    
while True:
    
    print ('The current SPY price is: ' + str(getPrice()))
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))
  




## def getOption():
    