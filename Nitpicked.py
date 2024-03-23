# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:56:17 2024

@author: craig
"""

import pandas as pd

data = pd.read_csv('for_nitpicker.dat', delimiter= '\t', header=None ) 

data.columns = ['Date', 'Time', 'Depth (m)', 'Temp (C)' , 'Salinity (PSU)']

data.to_csv('P1_CTD_20081129.dat', sep = '\t', index =False)


print(data)