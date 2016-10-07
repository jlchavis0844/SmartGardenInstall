import os.path #file check
import setupfiles.register # username registration
import setupfiles.tempSetup
import setupfiles.moistSetup
from setupfiles.tempSetup import tempSetup
list1 = []
list2 = []
goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']

list1, list2 = setupfiles.tempSetup.tempSetup()
print(list1)
print(list2)

list1, list2 = setupfiles.moistSetup.moistSetup()
print(list1)
print(list2)
#start to registration process
# if os.path.isfile("./gardenData.conf") == False:
#     print("No install detected, do you want to run the setup process?")
#     answer = raw_input("Enter Y to cotinue, anything else to quit\n")
#     print(answer in goodAnswers)
#     if (answer in goodAnswers):
#         register.register()
#     else:
#         print("Goodbye!")
#         exit()
# else:
#     installed = True