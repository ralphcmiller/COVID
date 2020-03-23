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
counter = -1
input_strike = input('Enter the strike price you would like to monitor: $')
input_strike = input_strike + '.00'
print (' ')
onStartup = 0


def getPrice():
    
    strikePrice = 0
    counter = -1
    r = requests.get('https://finance.yahoo.com/quote/SPY?p=SPY', verify = False)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').get_text()
##    CNG = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[1].find('span').get_text()
    r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY&date=1587081600', verify=False)

    while strikePrice!=input_strike:
        counter = counter + 1
        soup = bs4.BeautifulSoup(r.text,"lxml")
        strikePrice = soup.find_all('a',{'class': 'C($linkColor) Fz(s)'})[counter].text
        
    else:
        optionPrice = soup.find_all('td',{'class': 'data-col3 Ta(end) Pstart(7px)'})[abs(counter)].get_text()
        percentCng = soup.find_all('td',{'class': 'data-col7 Ta(end) Pstart(7px)'})[abs(counter)].find('span').get_text()
        IV = soup.find_all('td',{'class': 'data-col10 Ta(end) Pstart(7px) Pend(6px) Bdstartc(t)'})[abs(counter)].get_text()
        return price,strikePrice,optionPrice,percentCng,IV
        

while True:
    if onStartup == 0:
        a1,b1,c1,d1,e1 = getPrice()
        OG_price = float(a1)
        OG_premium = float(c1)
        onStartup=onStartup + 1
    else:
       a,b,c,d,e = getPrice()
       new_price = float(a)
       new_premium = float(c)
       
       PC_price = float((((new_price - OG_price)/abs(OG_price))*100))
       PC_premium = float((((new_premium - OG_premium)/abs(OG_premium))*100))
       
       print ('SPY Price:         $' + a + '    %CNG ' +str(PC_price))
       print ('Strike Price:      $' + b)
       print ('Premium Value:     $' + c + '     %CNG ' + str(PC_premium) + '     IV: ' + e)
       print (' ')
       
       time.sleep(15.0 - ((time.time() - starttime) % 15.0)) #15 sec interval