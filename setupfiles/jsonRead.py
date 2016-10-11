'''
Created on Oct 7, 2016

@author: James

'''
import json

def getJSON():
    tempNames =[]
    tempChan = []
    moistNames=[]
    moistChan=[]
    listOfLists = []
    
    with open("data.json", "r") as f:
        data = json.load(f)
    user = data['user']
    passwd = data['password']
    
    print data
    gKeys =data['Gardens'].keys()
    for x in range(len(gKeys)):
        for y in range(len(data['Gardens'][gKeys[x]])):
            listOfLists.append(data['Gardens'][gKeys[x]][y]\
                               [data['Gardens'][gKeys[x]][y].keys()[0]])
            
    print(listOfLists)
    
    for i in range(len(gKeys)):
        flexNum = i * 4
        tempNames = tempNames + listOfLists[flexNum+0]
        tempChan = tempChan + listOfLists[flexNum+1]
        moistNames = moistNames + listOfLists[flexNum+2]
        moistChan = moistChan + listOfLists[flexNum+3]
    
    return user, passwd, gKeys, tempNames, tempChan, moistNames, moistChan