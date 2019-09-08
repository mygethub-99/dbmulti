# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:21:42 2019
Pull DB data and then create dataframes for each freq band
@author: ow4253
"""
import pandas as pd
from dbconnect import (axiomdb, iqiDB)
#Call dbconnect to grab db data
iqi=iqiDB()
axiom=axiomdb()
#Create dataframe for each spectrum band
iqi_spectrum =iqi.freqMostUd.unique()
fl = []
for i in iqi_spectrum:
    if i == 'AWS':
        fl.append(i)
    elif i == 'WCS':
        fl.append(i)
    elif i == '700':
        x= '_700'
        fl.append(x)
    elif i == '1900':
        y= '_1900'
        fl.append(y)
f2 = iqi_spectrum.tolist()
[i for i in f2 if i is not None]

spdict=dict(zip(fl,f2))   
for k, v in spdict.items():
    exec("{}=iqi[iqi['freqMostUd']=='{}']" .format(k,v))
