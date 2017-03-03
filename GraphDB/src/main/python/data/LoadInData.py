'''
Created on 28 Feb 2017

@author: guytu
'''

from main.python.data.GraphDB import executeCypher
from src.main.python.data.CypherUtils import makeCreateNodeStatement
from src.main.python.data.DataPrep import dataPrep


stations, values = dataPrep("file:///C:/Users/guytu/Downloads/readings-full-2017-02-25.csv")

createStationsCypher = makeCreateNodeStatement(stations, "Station", "label")
#createValuesCypher = makeCreateNodeStatement(values, "Value", "value")
print(createStationsCypher)

executeCypher(createStationsCypher)
    