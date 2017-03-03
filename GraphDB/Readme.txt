Code used to load in data into neo4j. 

Included is:
  - code to send http get requests to urls
  - A first attempt at splitting values from stations
  - code to plot stations on google maps
  
Requires:
  - Neo4j
  - gmplot (install through pip)
  - pandas 
  
Note:
  - I have only tested this on flood data, we may need to make some mods to make this work for water quailty data.
  - It only works using Neo4j as the DB

To load data into neo4j, change the csv file path in LoadInData to a flood data csv stored on your machine and it should work.
