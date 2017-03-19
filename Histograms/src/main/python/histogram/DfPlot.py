'''
Created on 19 Mar 2017

@author: guytu
'''
from src.main.python.histogram.Plots import plotHistogram



def plotSingleHistogram(plot, df, readingColumn, numberOfBuckets, xLogScale, yLogScale, title):
    plot, histogram_Frequencies, histogram_Buckets = plotHistogram(plot, df[readingColumn],numberOfBuckets,xLogScale,yLogScale,title )
    return plot, {'frequencies': histogram_Frequencies, 'buckets': histogram_Buckets}
