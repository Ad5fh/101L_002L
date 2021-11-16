## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Clock
##Algorithm: The program below ask for the hours, the minutes and the seconds and then output everything in a clock format which means that the output is going to run undefinitely.
#################################################################################################################################

import time
#Defining a Class name Clock
class Clock:
#Defining a constructor with 4 parameters which are hours,minutes,seconds and clocktype.
    def __init__(self,hours=24,minutes=0,seconds=0,clocktype=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self.clocktype=clocktype
#Defining a tick method inside the Class which is going to increment the time clock based on seconds,minutes and hours.
    def tick(self):
        self.seconds+=1
        if self.seconds>=60:
            self.seconds-=60
            self.minutes+=1
        if self.minutes>=60:
            self.minutes-=60
            self.hours+=1
#Using getters to get hours      
    def getHours(self):
        return self.hours
#Using setters to set hours
    def setHours(self,hour):
        self.hours= hour%24
#Using getters to get minutes
    def getMinutes(self):
        return self.minutes
#Using setters to set minutes
    def setMinutes(self,minutes):
        self.minutes= minutes%60
#Using getters to get seconds   
    def getSeconds(self):
        return self.seconds
#Using setters to set seconds
    def setSeconds(self,seconds):
        self.seconds= seconds%60
#Using getters to get time   
    def getTime(self):
        return self.hours,self.minutes,self.seconds,self.clocktype
#Using setters to set time
    def setTime(self,time):
        self.hours,self.minutes,self.seconds,self.clocktype
#Defining __str__ method to override the constructor and display the time in format of hours:minutes:seconds and inserting am/pm according to the hour inserted.
    def __str__(self):
        if self.clocktype==0:
            return '{:02}:{:02}:{:02}'.format(self.hours,self.minutes,self.seconds)
        else:
            if self.hours>=12:

                typeclock='pm'
            else:
                typeclock='am'
            return '{:02}:{:02}:{:02} {}'.format(self.hours,self.minutes,self.seconds,typeclock)
#Main Function        
hours=int(input("What is the current hour ==> "))
minutes=int(input("What is the current minute ==> "))
seconds=int(input("What is the current second ==> "))
clock=Clock(hours,minutes,seconds,1)
#Creating an object of Clock class and keeping it in a while loop so that it will run forever.
while True:
    print(clock)
    clock.tick()
    time.sleep(1)
    
    

