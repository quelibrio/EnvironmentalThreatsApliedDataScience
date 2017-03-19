'''
Created on 19 Mar 2017

@author: guytu
'''
import pandas as pd
import os


def getCsvData(csv):
    print(os.environ['PYTHONPATH'])
    return pd.read_csv(os.path.abspath(csv))