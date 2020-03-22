# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:27:39 2020

@author: Ralph

This program is designed to monitor an options premium price given (Date and Strike)
give a readout of the precentage change from high

"""
import random
option = 100   ##random.randint(1, 5)
PC = 0
p_PC = 0
PC_high = 0
prev_option = 1
pp_o = 1

## get option data function

##get time
while option != prev_option:

## Calculate % change and % change from high

     PC = float((((prev_option - pp_o)/abs(pp_o))*100))

     print ('O: $' , option)
     print ('PC: ',PC,('%'))
     print ('PC_high: ',PC_high)
     print ("prev_option: $",prev_option)
     print (' ')
     prev_option = prev_option + 1
else:
     
     print ('wut')
     print ('Your option price is now equal to the previous option price')
     print (' ')
     print ('O: $' , option)
     print ('PC: ',PC,('%'))
     print ('PC_high: ',PC_high)
     print ("prev_option: $",prev_option)
     print (' ')



