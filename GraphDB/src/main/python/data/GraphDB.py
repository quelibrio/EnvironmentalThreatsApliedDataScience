'''
Created on 28 Feb 2017

@author: guytu
'''
from neo4j.v1 import GraphDatabase
from neo4j.v1 import basic_auth


host = "bolt://localhost"
port = "7687"
username = "neo4j"
password = "password_123"


def executeCypher(cypher):
    print(cypher)
    driver = GraphDatabase.driver("{}:{}".format(host, port), auth=basic_auth("%s" % username, "%s" % password))
    session = driver.session()
    
    result = session.run(cypher)
    session.close()
    return result
                                  

