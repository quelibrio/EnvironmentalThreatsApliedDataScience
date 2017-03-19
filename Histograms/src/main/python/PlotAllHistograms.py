'''
Created on 19 Mar 2017

@author: guytu
'''

from src.main.python.histogram.DfPlot import plotSingleHistogram
import matplotlib.pyplot as plt
from src.main.python.data.Utils import getCsvData



df = getCsvData("../resources/W-2016-M.csv")
plot = plt
histograms = {}
numberOfBuckets = 100
xLogScale = True
yLogScale = True
measurementColumn = 'result'
for i in df['determinand.label'].unique():
    print(i)
    title = "{} distribution".format(i) 
    sub_df = df[df['determinand.label'] == i]
    if any(sub_df['result'] <= 0):
        xLogScale = False
    else:
        xLogScale = True
    if len(sub_df[measurementColumn]) > 1:
        plot, histograms[i] = plotSingleHistogram(plot, sub_df, measurementColumn ,numberOfBuckets,xLogScale,yLogScale,title )
plot.show()
