'''
Created on 2 Mar 2017

@author: guytu
'''
import gmplot #Install from PIP

def plotOnGoogleMap(file, latitudes, longitudes):
    gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
    gmap.scatter(latitudes, longitudes, 'Blue', size=1000, marker=False)
    gmap.draw(file)
