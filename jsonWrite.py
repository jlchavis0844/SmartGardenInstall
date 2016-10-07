"""
Created on Oct 6, 2016

@author: James
"""
import json

dataString = {
    "user": "testUser",
    "password": "password1",
    "Garden": {
        "Name" : "defaultGarden",
        "hardware" : {
            "tempNames" : ["temp0", "temp1"],
            "tempChan"  : [0,1],
            "moistName" : ["moist0", "moist1"],
            "moistChan" : [19, 18]
             }
        }
}

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(dataString, f)
    
# Reading data back
with open('data.json', 'r') as f:
     data = json.load(f)
     
     print(data)