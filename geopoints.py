"""
Created on Mon Sep  9 16:15:41 2019
Creates lat-long point data based on site file, a buffer and then bounds of buffer. Also creates geo data for iqi dataframes
@author: ow4253
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
   
def bounds():
    path =r'C:\Users\ow4253\Documents\development\vertica\dbscripts\sitelist.csv'
    filein = pd.read_csv(path)
    geometry=[Point(xy) for xy in zip(filein['LONGITUDE'], filein['LATITUDE'])]
#The gpd.points_from_xy rapper doesn't work. I had to use a manuel zip method
#geofile=gpd.GeoDataFrame(filein, geometry=gpd.points_from_xy(filein.Longitude, filein.Latitude))
    crs={'init':'epsg:4326'}
    #geofile=gpd.GeoDataFrame(filein, crs=crs, geometry=geometry)
#Create geoseries of point data found in geometry 
    dataGeo=gpd.GeoSeries(geometry, index=filein['USID'])
#Create a buffer around the point data with a specific distance
#This is what you will set as your sites bounds to run your iqi query on
    buffer=dataGeo.buffer(.03)    
#Create the bounds min and max of x and y
    bounds=buffer.bounds
    return bounds
    
def buffer():
    path =r'C:\Users\ow4253\Documents\development\vertica\dbscripts\sitelist.csv'
    filein = pd.read_csv(path)
    geometry=[Point(xy) for xy in zip(filein['LONGITUDE'], filein['LATITUDE'])]
    #crs={'init':'epsg:4326'}
    #geofile=gpd.GeoDataFrame(filein, crs=crs, geometry=geometry)
#Create geoseries of point data found in geometry 
    dataGeo=gpd.GeoSeries(geometry, index=filein['USID'])
#Create a buffer around the point data with a specific distance
#This is what you will set as your sites bounds to run your iqi query on
    buffer=dataGeo.buffer(.03)
    return buffer

def geosites():
    path =r'C:\Users\ow4253\Documents\development\vertica\dbscripts\bhamsites.csv'
    filein = pd.read_csv(path)
    geometry=[Point(xy) for xy in zip(filein['LONGITUDE'], filein['LATITUDE'])]
    crs={'init':'epsg:4326'}
    geofile=gpd.GeoDataFrame(filein, crs=crs, geometry=geometry)
    return geofile

def geoiqi(df,site):
    geometry=[Point(xy) for xy in zip(df.long, df.lat)]
    crs={'init':'epsg:4326'}
    return (exec("{}=gpd.GeoDataFrame(df, crs=crs, geometry=geometry)" .format(site)))
