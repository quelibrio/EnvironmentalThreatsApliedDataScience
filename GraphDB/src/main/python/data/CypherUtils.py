'''
Created on 28 Feb 2017

@author: guytu
'''


def makeCreateNodeStatement(df, nodeType, key):
    statement = "create {}"
    nodeStatement = "({}:{} {})"
    nodeStatements = []
    
    for i,row in df.iterrows():
        
        var = nodeType.lower() + str(i)     
        attributes = "{"+', '.join("{!s}:{!r}".format(key,str(val)) for (key,val) in row.to_dict().items())+"}"
        nodeStatements.append(nodeStatement.format(var, nodeType ,attributes))
    statement = statement.format(",".join("{}".format(item) for (item) in nodeStatements))
    return statement
    
def makeCreateEdge(node1, node1Type, node2, node2Type, edgeKey, edgeType, edgeProperties):
    matchStatement = "match ({}:{}),({}:{})".format(node1, node1Type, node2, node2Type)
    createStatement = "create ({})-[{}:{} {}]->({})".format(node1, edgeKey, edgeType, edgeProperties, node2)
    statement = "{} {}".format(matchStatement, createStatement)
    return statement
    
