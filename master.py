# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:16:01 2019

@author: ow4253
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

from geopoints import buffer, geosites, bounds, geoiqi
from dbconnectFunc import iqiDB
from readshp import highway
#Create map of existing sites, buffers, bounds, iqi
dates=['201907','201908']
sites=geosites()
buf=buffer()
bound=bounds()
highway=highway()

#Execute iqi query on each new site based on bounds, name it by usid
#Create GeoDataFrame with lat and long geometry for plotting
for i, row in bound.iterrows():
    bd=row['minx'],row['miny'],row['maxx'],row['maxy']
    site='_'+str(i)
    df=iqiDB(bd,dates)
    exec("{}=geoiqi(df)" .format(site))
#Create plots
for i, row in bound.iterrows():
    site = '_'+str(i)
    #fig= plt.figure()
    plt.rcParams['figure.figsize'] = (4,3)
    plt.rcParams['figure.dpi'] = 150
    ax=sites.plot(color='red',markersize=5)
    exec("ax={}[{}['avg_rsrp'] > -105].plot(ax=ax,markersize = 2, color = 'blue', marker = 'o', alpha=.05)" .format(site,site))
    sites.plot(ax=ax, color='red',markersize=5)
    highway.plot(ax=ax, color = 'black', alpha=.5)
    black_label = mpatches.Patch(color='black', label='-105RSRP 10Meter IQI')
    plt.legend(handles=[black_label])
    ax.set_xlim([row['minx'],row['maxx']])
    ax.set_ylim([row['miny'],row['maxy']])
    plt.show()
    plt.savefig(r'C:\Users\ow4253\Documents\development\vertica\dbscripts\plots\{}.pdf'.format(site))
