'''
Created on 28 Feb 2017

@author: guytu
'''

from urllib import request
import json

def getUrlData(url):
    connection = request.urlopen(url)
    response = connection.read()
    connection.close()
    return response

def convertToJsonDict(arg):
    return json.loads(arg.decode('utf-8'))
    
