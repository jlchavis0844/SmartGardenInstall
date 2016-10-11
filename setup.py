import os.path #file check
import setupfiles.fullSetup
list1 = []
list2 = []
goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']
boolStop = False



#start registration process
if os.path.isfile("./data.json") == False:
    print("No install detected, do you want to run the complete setup process?")
    answer = raw_input("Enter Y to continue, anything else to quit\n")
    print(answer in goodAnswers)
    
    if (answer in goodAnswers):
        setupfiles.fullSetup.fullSetup()
        exit()
        
# print('What would you like to do instead?')
# print('1. add a new garden')
# print('2. delete a garden')
# print('3. view config file to adjust gardens')
# 
# answer = raw_input('Enter 1-3 : \t')
# 
# while boolStop == False:
#     if answer == 1:
#         pass
#     elif answer == 2:
#         pass
#     elif answer == 3:
#         pass
#     else:
#         pass
