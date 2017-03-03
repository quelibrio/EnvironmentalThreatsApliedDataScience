'''
Created on 28 Feb 2017

@author: guytu
'''
from main.python.data.DataUtils import convertToJsonDict, getUrlData
import pandas as pd


def fillStationData(stations):
    for i, row in stations.iterrows(): 
        print(i)
        url = row['station']
        print(url)
        data = convertToJsonDict(getUrlData(url))
        try: 
            lat = data['items']['lat']
        except KeyError:
            lat = None
        try: 
            longitude = data['items']['long']
        except KeyError:
            longitude = None
        try:
            gridReference = data['items']['gridReference']
        except KeyError:
            gridReference = None   
        stations.loc[i,'lat'] = str(lat)
        stations.loc[i,'long'] = str(longitude)
        stations.loc[i, 'gridReference'] = str(gridReference)
    return stations
    
def dataPrep(csv):
    df = pd.read_csv(csv)
    stations = getStations(df)
    stations = fillStationData(stations)
    values = getValues(df)
    print(values)
    return stations, values
     
         
def getStations(df):
    stations = df[['station','label','stationReference','qualifier']]
    #stations.set_index('stationReference', inplace=True)
    stations = stations.drop_duplicates(keep='first')
    return stations

def getValues(df):
    values = df[['value','valueType','unitName','parameter','stationReference', "dateTime"]]
    return values

    