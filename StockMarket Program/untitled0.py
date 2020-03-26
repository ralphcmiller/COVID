# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:19:36 2020

@author: Ralph
"""
import bs4
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


r = requests.get('https://finance.yahoo.com/quote/SPY/options?p=SPY&date=1587081600', verify=False)
soup = bs4.BeautifulSoup(r.text,"lxml")

t =soup.find_all('a',{'class': 'C($linkColor) Fz(s)'}).text
print (t)