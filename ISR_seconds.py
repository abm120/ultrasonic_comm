import time                          #Importing 'time' library
import datetime                     #Importing 'datetime' library
from datetime import timedelta     #Importing 'timedelta' class from library

t1 = datetime.datetime.now().time()  #accessing current system time
print t1
#"""
print "seconds = ",t1.second                     #printing seconds value of current time
count1 = 1                           #Initializing count variable

while (count1 <= 10):                                                      #Loop for 10 iterations
    current_second = datetime.datetime.now().time().second
    if(current_second == (t1.second + count1)):     #check & compare current seconds value
        print "printing at ", current_second , " seconds"                      #Print every second 
        count1 = count1 + 1                                                #Increment count
        
#"""