#this file will take input from the user to get sensor names and channels
#this will return two lists, the moisture sensor name list and the channel list
#return sensorName list then sesorChan list

GardenName = ""

def moistSetup():
    moistNames = []
    moistChan = []
    stopBool = False
    while stopBool == False:    
        tempVal = raw_input('enter the sensor name, \'exit\' to quit\n')
        if tempVal == 'exit':
            print('exiting sensor input\n')
            stopBool = True;
        else:
            moistNames.append(tempVal)
            tempVal = raw_input('Enter the channel ' + tempVal + ' is on\n')
            moistChan.append(tempVal)
    #end while loop
    return moistNames, moistChan

def tempSetup():
    tempNames = []
    tempChan = []
    stopBool = False
    while stopBool == False:    
        tempVal = raw_input('enter the sensor name, \'exit\' to quit\n')
        if tempVal == 'exit':
            print('exiting sensor input\n')
            stopBool = True;
        else:
            tempNames.append(tempVal)
            tempVal = raw_input('Enter the channel ' + tempVal + ' is on\n')
            tempChan.append(tempVal)
    #end while loop
    return tempNames, tempChan
            
def makeGarden():
    GardenName = raw_input('Enter the name for this garden\n')
    gDesc = raw_input('Enter a description for this garden\n')
    print('Please enter information for the temp sensors\n')
    tempName, tempChan = tempSetup()
    print('Please enter information for the moisture sensors\n')
    moistNames, moistChan = moistSetup()
    return GardenName, tempName, tempChan, moistNames, moistChan, gDesc

#print(makeGarden())
    