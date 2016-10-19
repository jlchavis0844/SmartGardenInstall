"""
Created on Oct 6, 2016

@author: James
"""

import json, urllib2, datetime
import setupfiles.gardenSetup
import setupfiles.register
import Adafruit_Python_DHT.ez_setup
import Adafruit_Python_MCP3008.ez_setup


def sendSensor(userS, passS, sName, gName):
    urlBaseS = 'http://76.94.123.147:49180/addSensor.php?user=' \
            + userS + '&password=' + passS + '&sName=' + sName.replace(" ", "%20") \
            + '&gName=' + gName.replace(" ", "%20")
    resp = urllib2.urlopen(urllib2.Request(urlBaseS));
    
    print resp.read();

def makeGarden(gUser, gPass, gName, gDesc):
    urlBaseS = 'http://76.94.123.147:49180/addGarden.php?user=' \
            + gUser + '&password=' + gPass + '&gName=' + gName.replace(" ", "%20") \
            + '&gDesc=' + gDesc.replace(" ", "%20")
    resp = urllib2.urlopen(urllib2.Request(urlBaseS))
    
    print resp.read();

def installFiles():
    print('installing DHT files')
    Adafruit_Python_DHT.ez_setup.main()
    print('installing MCP files')
    Adafruit_Python_MCP3008.ez_setup.main()
    fullSetup()

def fullSetup():
    
    stopBool = False
    data = {}
    tempNames= {}
    tempChan= {}
    moistNames= {}
    moistChan={}
    garden ={}
    goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']
    
    user, password = setupfiles.register.register()
    data["user"] = user
    data["password"] = password
    data["updated"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    while stopBool == False:
        gName, tempNames, tempChan, moistNames, moistChan, gDesc = setupfiles.gardenSetup.makeGarden()
        
        garden[gName] = [{"TempNames" : tempNames},\
                        {"TempChan" :  tempChan},\
                        {"MoistNames" : moistNames},\
                        {"MoistChan" : moistChan}]
        
        #print(garden)

        data["Gardens"] = garden
        #print(data)
        if(gName != None):
            makeGarden(user, password, gName, gDesc)
        
        if(len(tempNames) > 0):
            for x in range(0, len(tempNames)):
                sendSensor(user, password, tempNames[x], gName)
                
        if(len(moistNames) > 0):
            for x in range(0, len(moistNames)):
                sendSensor(user, password, moistNames[x], gName)
                
        
            
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

