import time                          #Importing 'time' library
import datetime                     #Importing 'datetime' library
from datetime import timedelta     #Importing 'timedelta' class from library

t1 = datetime.datetime.now().time()  #accessing current system time
print t1
#"""
print "microseconds = ",t1.microsecond                     #printing seconds value of current time
count1 = 1                           #Initializing count variable

while (count1 <= 10):                                                      #Loop for 10 iterations
    current_microsecond = datetime.datetime.now().time().microsecond
    #if(current_second == (t1.second + count1)):     #check & compare current seconds value
    print "printing at ", current_microsecond , " microseconds"                      #Print every second 
    count1 = count1 + 1                                                #Increment count
        
#"""
#time.sleep(1)
# printing a number of times to test minimum time difference allowed between execution of 2 consecutive statements...
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()
print datetime.datetime.now().time()


#time.sleep(1)

t2 = datetime.datetime.now().time()  #accessing current system time
print t2
#"""
print "microseconds = ",t1.microsecond                     #printing seconds value of current time
count1 = 1                           #Initializing count variable
time_increment = 1000
delta_time = 100

while (count1 <= 10):                                                      #Loop for 10 iterations
    current_microsecond = datetime.datetime.now().time().microsecond
    if((current_microsecond > (t1.microsecond + time_increment - delta_time)) and (current_microsecond < (t1.microsecond + time_increment + delta_time))):     #check & compare current seconds value
        print "printing at ", current_microsecond , " microseconds"                      #Print every second 
        count1 = count1 + 1
        time_increment += 1000                                              