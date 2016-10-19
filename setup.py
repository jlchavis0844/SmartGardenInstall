import os.path #file check
import setupfiles.fullSetup
list1 = []
list2 = []
goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']
boolStop = False



#start registration process
if os.path.isfile("./data.json") == False:
    print("No install detected, do you want to run the complete setup process?")
    print("This will install all necessary files and run registration and setup")
    answer = raw_input("Enter Y to continue, anything else to continue\n")
    
    if (answer in goodAnswers):
        setupfiles.fullSetup.installFiles()
        
print("Enter Y to continue with the setup without install")
answer = raw_input("Enter anything else to quit")
if(answer in goodAnswers):
    setupfiles.fullSetup.fullSetup()
    
if os.path.isfile("./data.json") == True:
    answer = raw_input("would you like to launch the config file to change values?")
    if(answer in goodAnswers):
        os.system("start data.json")
       
print 'Goodbye'
exit()