# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:16:01 2019

@author: ow4253
"""
from geopoints import buffer, geosites, bounds
from dbconnectFunc import iqiDB
dates=['201907','201908']

#Create map of existing sites, buffers and bounds
sites=geosites()
buf=buffer()
bound=bounds()

#Execute iqi query on each new site, name it by usid and boundary
for i, row in bound.iterrows():
    bd=row['minx'],row['miny'],row['maxx'],row['maxy']
    site='_'+str(i)
    exec("{}=iqiDB({},{})" .format(site,bd,dates))
    
 

#Plot sites and boundary of each site    
ax=sites.plot(color='blue', edgecolor='black',markersize=5)
buf.plot(ax=ax, color='red',alpha=0.7)
