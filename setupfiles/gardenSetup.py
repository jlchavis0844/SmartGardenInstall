#this file will take input from the user to get sensor names and channels
#this will return two lists, the moisture sensor name list and the channel list
#return sensorName list then sesorChan list
tempNames = []
tempChan = []
moistNames = []
moistChan = []
GardenName = ""

def moistSetup():
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

def tempSetup():
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
            
def makeGarden():
    GardenName = raw_input('Enter the name for this garden\n')
    print('Please enter information for the temp sensors\n')
    tempSetup()
    print('Please enter information for the moisture sensors\n')
    moistSetup()
    