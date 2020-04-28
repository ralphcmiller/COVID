# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:57:21 2020

@author: Ralph

    This program takes barchart.com's unusual options tracker .csv file and will scrape through the data 
    given user defined inputs to produce organized information for the user

    To use this program you must goto: 
    
        https://www.barchart.com/options/unusual-activity/stocks?orderBy=tradeTime&orderDir=asc
    
    and download the .csv file and save the file in the folder where the program is contained,
    you must then rename the file to 'options_activity' for the program to handle the file correctly.
    
"""
import csv
counter = 0
size = 0
sortTicker = []
'array that contains the returned values, structured w/ 15 rows'
'[0      1      2     3       4         5    6    7      8    9     10   11        12      13  14]'
'symbol, price, type, strike, exp date, DTE, bid, midpt, ask, last, vol, open int, vol/OI, IV, time'
results = [] 
tickerArray = []
sortedArrayPut = []
sortedArrayCall = []
sortedTickerArray = []
ticker = input('what ticker do you want to look at? \n')
def getTicker(): #puts all tickers into an array then sorts the duplicates to return a list of all tickers in the csv
    with open('options_activity.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)    
        for line in csv_reader:
            tickerArray.append(line[0])
        size = len(tickerArray) -1
        counter = size    
        while counter > 0:
            sortTicker = tickerArray[counter]
            tickerArraySize = len(tickerArray) - 1
            while tickerArraySize > 0:
                if tickerArray[tickerArraySize] == sortTicker:
                    tickerArraySize -= 1
                
                else:
                    sortedTickerArray.append
                    tickerArraySize -= 1
            counter -= 1
                    
            
            



def getArray(): #takes the csv file and puts the chosen ticker into an array
    with open('options_activity.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == str(ticker):
            
                #print (line)
                results.append(line)


def C2P_ratio(): #sorts the array and calculates the Call to Put ratio on the ticker.
    
    size = len(results) -1
    counter = size
    while counter > 0:
        sort = results[counter]
        if sort [2] == ('Put'):
            sortedArrayPut.append(sort)
            counter -= 1
        else:
            sortedArrayCall.append(sort)
            counter -= 1
    
    c2p = len(sortedArrayCall)/len(sortedArrayPut)
    print ('The call to put ratio for ' + ticker + ' = ' + str(round(c2p, 2)))

getTicker()
getArray()
C2P_ratio()
