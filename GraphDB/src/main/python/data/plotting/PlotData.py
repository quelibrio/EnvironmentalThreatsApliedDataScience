'''
Created on 2 Mar 2017

@author: guytu
'''

from main.python.data.GraphDB import executeCypher
from src.main.python.data.plotting.GoogleMapPlotting import plotOnGoogleMap


latitudes = []
longitudes = []

result = executeCypher("match (n) return n.lat as lat, n.long as long")

for record in result:
    latitude = record['lat']
    longitude = record['long']
    try:
        latitude = float(latitude)
        longitude = float(longitude)
        latitudes.append(latitude)
        longitudes.append(longitude)
    except ValueError:
        pass
        
print(latitudes)
print(longitudes)
plotOnGoogleMap("flood-stations.html", latitudes, longitudes)