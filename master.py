from geopoints import buffer, geosites, bounds, geoiqi
from dbconnectFunc import iqiDB
#Create map of existing sites, buffers, bounds, iqi
dates=['201907','201908']
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
    exec("{}=geoiqi(df)" .format(site))

#Plot sites and boundary of each site
    
ax=sites.plot(color='blue', edgecolor='black',markersize=5)
buf.plot(ax=ax, color='red',alpha=0.7)
