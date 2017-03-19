'''
Created on 19 Mar 2017

@author: guytu
'''

import numpy


def plotHistogram(plot, values, numberOfBuckets, xAxisLogScale, yAxisLogScale, title):
    'Plots a histogram with mean and median lines, with or without log scales'
    'Requires matplotlib plot to be passed in'
    'returns resulting plot, frequencies and bins in tuple'
    mean = values.mean()
    median = values.median()
    xLabel = "Buckets"
    yLabel = "Frequency"
    plotLogScale = False
    buckets = numberOfBuckets
    
    if yAxisLogScale:
        plotLogScale = True
        yLabel = "Frequency (log scale)"
    if xAxisLogScale:
        buckets = numpy.logspace(numpy.log10(min(values) - min(values)/len(values) ),numpy.log10(max(values) + min(values)/len(values)),numberOfBuckets)
        xLabel = "Buckets (log scale)"
    figureNumbers = plot.get_fignums()
    if not figureNumbers:
        figureNumber = 1
    else:
        figureNumber = max(plot.get_fignums()) + 1
    
    plot.figure(figureNumber)
    histogram = plot.hist(values,bins=buckets,log=plotLogScale)
    meanLine = plot.axvline(mean, color='r', linestyle='dashed', linewidth=5, label='Mean')
    medianLine = plot.axvline(median, color='y', linestyle='dashed', linewidth=5, label='Median' )
    if xAxisLogScale:
        plot.gca().set_xscale("log")
    plot.ylim(0.1)
    plot.xlabel(xLabel)
    plot.ylabel(yLabel)
    plot.legend(handles=[meanLine, medianLine])
    plot.title(title)
    return plot, histogram[0], histogram[1]
        