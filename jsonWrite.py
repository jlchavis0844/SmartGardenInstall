"""
Created on Oct 6, 2016

@author: James
"""
import json

data = {}
hardware = {}
tempNames= {}
tempChan= {}
moistNames= {}
moistChan={}
name=garden ={}
tempNames["tempNames"] = ["temp0", "temp1"]
tempChan["tempChan"] = [0,1]
moistNames["moistNames"] = ["moist0", "moist1"]
moistChan["moistChan"] = [19,18]

garden["hardware"] = [tempNames, tempChan,moistNames,tempChan]

garden["Name"] = "defaultGard"
print(garden)
data["user"] = "testUser"
data["password"] = "password1"
data["Garden"] = garden
print(data)
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    data = json.load(f)

print(data)