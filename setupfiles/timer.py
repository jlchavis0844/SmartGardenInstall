#!/usr/bin/env python
'''
Created on Oct 31, 2016

@author: James
'''
import os #for path finding
from crontab import CronTab
import itertools
goodAnswers = ['y', 'Y', 'yes', 'Yes', 'YES']
global command 
command = os.getcwd() + "/takeReadings.py"
#check if there is a valid number
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def peek(iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], iterable)

def scheduleJob():
    cron = CronTab(user=True)
    currentjobs = cron.find_command('takeReadings')
    res = peek(currentjobs)
    if res is None:
        makeJobs()
    else:
        print("Aleady configured to take the following readings")
        print("min hr * * * command")
        for job in currentjobs:
            print(job)
        
        answer = raw_input("do you want to overwrite this schedule?")
        if(answer in goodAnswers):
            cron.remove_all(command = command)
            cron.write()
            print("deleting and starting new")
            makeJobs()
        else :
            print("exiting scheduler")
            
#makes 2 entries in the crontab with the given specifications
def makeJobs():
    cron = CronTab(user=True)
    print("Scheduling automatic readings twice daily")
    
    cont = False
    while(cont == False):
        hour = raw_input("For the first reading, enter the hour in military time (0-23)\n")
        cont = is_number(hour)
        if(not cont):
            print("Please enter a valid number")
            cont = False
        hour = int(hour)
        if(hour < 0 or hour > 23):
            print("Please enter between 0 and 23")
            cont = False
    cont = False
    
    while(cont == False):
        min = raw_input("For the first reading, enter the minute (0 - 59)\n")
        cont = is_number(min)
        if(not cont):
            print("Please enter a valid number")
            cont = False
        min = int(min)
        if(min < 0 or min > 59):
            print("Please enter between 0 and 59")
            cont = False

    cont = False
    
    while(cont == False):
        interval = raw_input("Interval between first and second readings in hours (usually 12)\n")
        cont = is_number(interval)
        if(not cont):
            print("Please enter a valid number")
            cont = False
        
        interval = int(interval)
        if(interval < 1 or interval > 12):
            print("Please enter a valid number")
            cont = False

    print("scheduling readings for daily at " + str(hour) + ":" + str(min))
    print("and " + str(hour + interval ) + ":" + str(min))
    
    command = os.getcwd() + "/takeReadings.py"
    print("setting the following command: " + command)
 
    time = str(min) + " " + str(hour) + " * * *"
    job = cron.new(command)
    job.setall(time)
    cron.write()
    
    time = str(min) + " " + str(hour + interval) + " * * *"
    job = cron.new(command)
    job.setall(time)
    cron.write()