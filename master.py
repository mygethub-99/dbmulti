# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:16:01 2019

@author: ow4253
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon

from geopoints import buffer, geosites, bounds
from dbconnectFunc import iqiDB
#from iqibands import uniband
dates=['201907','201908']

#Create map of existing sites, buffers and bounds
sites=geosites()
buf=buffer()
bound=bounds()
usid_list=[]
#Execute iqi query on each new site based on bounds, name it by usid
#Create GeoDataFrame with lat and long geometry for plotting
for i, row in bound.iterrows():
    bd=row['minx'],row['miny'],row['maxx'],row['maxy']
    site='_'+str(i)
    df=iqiDB(bd,dates)
    usid_list.append(i)
    geometry=[Point(xy) for xy in zip(df.long, df.lat)]
    crs={'init':'epsg:4326'}
    exec("{}=gpd.GeoDataFrame(df, crs=crs, geometry=geometry)" .format(site))
    


#Plot sites and boundary of each site    
ax=sites.plot(color='blue', edgecolor='black',markersize=5)
buf.plot(ax=ax, color='red',alpha=0.7)
