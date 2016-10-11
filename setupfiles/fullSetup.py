"""
Created on Oct 6, 2016

@author: James
"""

import json
import setupfiles.register.old
import setupfiles.gardenSetup
import Adafruit_Python_DHT.ez_setup
import Adafruit_Python_MCP3008.ez_setup

def fullSetup():
    print('installing DHT files')
    Adafruit_Python_DHT.ez_setup.main()
    print('installing MCP files')
    Adafruit_Python_MCP3008.ez_setup.main()
    
    stopBool = False
    data = {}
    tempNames= {}
    tempChan= {}
    moistNames= {}
    moistChan={}
    garden ={}
    goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']
    
    user, password = setupfiles.register.old.old()
    data["user"] = user
    data["password"] = password
    
    while stopBool == False:
        gName, tempNames, tempChan, moistNames, moistChan = setupfiles.gardenSetup.makeGarden()
        
        garden[gName] = [{"TempNames" : tempNames},\
                        {"TempChan" :  tempChan},\
                        {"MoistNames" : moistNames},\
                        {"MoistChan" : moistChan}]
        
        #print(garden)

        data["Gardens"] = garden
        #print(data)
        
        answer = raw_input("Would you like to add another Garden?\n Yes or No\t")
        
        if (answer in goodAnswers):
            print("adding another garden")
        else:
            print("ending setup, writing to data.json")
            stopBool = True
    #end while loop
    
    #write to a JSON file    
    with open("data.json", "w") as f:
        json.dump(data, f)
    
    #with open("data.json", "r") as f:
        #data = json.load(f)
    #print(data)
    
    return data