import pandas as pd


filename = 'full_2017-03-12.csv'
filename2 = 'full_2017-03-12_2017-03-14.csv'

df = pd.read_csv(filename)

print df.head()
