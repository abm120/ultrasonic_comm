import time                          #Importing 'time' library
import datetime                     #Importing 'datetime' library
from datetime import timedelta     #Importing 'timedelta' class from library

t1 = datetime.datetime.now().time()  #accessing current system time

#"""
print t1.second                     #printing seconds value of current time
count1 = 1                           #Initializing count variable

while (count1 <= 10):                                                      #Loop for 10 iterations
    if(datetime.datetime.now().time().second == (t1.second + count1)):     #check & compare current seconds value
        print "printing after ", count1 , " seconds"                      #Print every second 
        count1 = count1 + 1                                                 #Increment count
#"""
        
count2 = 1
t2 = datetime.datetime.now().time()  #accessing current system time
ms = t2.microsecond
print ms
ms = ms + 100         
while (count2 <= 5):                                                                #Loop for 5 iterations
    checkms = datetime.datetime.now().time().microsecond
    if ((checkms > (ms-1)) | (checkms < (ms+1))):                             #check & compare current seconds value
    #if (checkms == ms):                             #check & compare current seconds value
        print datetime.datetime.now().time().microsecond                           #Print every second 
        count2 = count2 + 1                                                           #Increment count        
        ms = ms + 100
"""
"""
t3 = datetime.datetime.now().time()  #accessing current system time
ms = t3.microsecond
s = t3.second

while(1):    
    if ((datetime.datetime.now().time().microsecond - t3.microsecond) % 1000 == 0):
        print datetime.datetime.now().time().microsecond
        time.sleep(0.01)
        if(datetime.datetime.now().time().second == (s + 5)):
            break
"""            
t4 = datetime.datetime.now().time()  #accessing current system time

#"""
print t4.microsecond                     #printing seconds value of current time
count4 = 1                           #Initializing count variable

while (count4 <= 10):                                                      #Loop for 10 iterations
    if(datetime.datetime.now().time().microsecond == (t1.second + 20*count4)):     #check & compare current seconds value
        print "printing after ", (20*count4) , " microseconds"                      #Print every second 
        count4 = count4 + 1                                                 #Increment count
        #"""