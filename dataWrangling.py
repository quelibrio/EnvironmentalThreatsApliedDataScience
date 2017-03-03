import json
import requests
import pandas as pd
import matplotlib as plt

root = "http://environment.data.gov.uk/flood-monitoring"

# -- FLOOD WARNINGS ---
flood_warning_allerts = root + "/id/floods" # all flood warning and allerts
flood_areas = root + "/id/floodAreas" # flood areas to which warnings and alerts can apply

response = requests.get(flood_warning_allerts)
jsonData = response.json()

print "status code: " + str(response.status_code)
print "keys: " + str(jsonData.keys())


df_original = pd.DataFrame(jsonData['items']) # discard context and metadata, create DataFrame from items
print df_original.columns

# quick statistical summary of the data
print df_original.describe()

# select columns
df = df_original[['eaAreaName', 'eaRegionName', 'floodArea', 'isTidal', 'severity', 'severityLevel']]

# sort columns by severity level
sorted = df.sort(columns='severityLevel', ascending=False)
print sorted

# group
grouped = df.groupby(['eaAreaName', 'eaRegionName', 'isTidal']).mean()
print grouped

# select rows where isTidal == true
print df[df['isTidal'] == True]['eaRegionName']