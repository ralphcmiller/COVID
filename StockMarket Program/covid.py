# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:41:33 2020

@author: Ralph
"""

import bs4
import requests
from bs4 import BeautifulSoup

def getUSCases():
    
    r = requests.get('https://www.worldometers.info/coronavirus/', verify = False)
    soup = bs4.BeautifulSoup(r.text,'html')
    activeCases = soup.find_all('td',{'style':'font-weight: bold; text-align:right'})[10].text
    recoveredCases = soup.find_all('td',{'style':'font-weight: bold; text-align:right'})[11].text
    totalDeaths = soup.find_all('td',{'style':'font-weight: bold; text-align:right'})[12].text
    return activeCases,recoveredCases,totalDeaths
    

    
def getGlobalCases():
    
    r = requests.get('https://coronavirus.jhu.edu/map.html', verify = False)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    activeCases= soup.find_all('')
    recoveredCases = soup.find_all('')
    totalDeaths = soup.find_all('')
    return activeCases,recoveredCases,totalDeaths


