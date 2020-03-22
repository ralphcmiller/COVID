# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:29:39 2020

@author: Ralph
"""
# timer that goes off every 30 seconds

import time
starttime=time.time()
while True:
  print ("tick")
  time.sleep(30.0 - ((time.time() - starttime) % 30.0))