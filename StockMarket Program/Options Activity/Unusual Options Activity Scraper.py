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

with open('options_activity.csv', 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    for line in csv_reader:
        if line[0] == str('ZM'):
        
            print (line[2])
        else:
            
            counter = counter + 1
