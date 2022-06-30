import time
import winsound
import sys
import wave
import math
import struct
import random
import argparse
import matplotlib.pyplot as plt
from itertools import *

def sine_wave(frequency0=1000.0, frequency1 = 5000.0, sample_rate=44100, amplitude=0.5):        #changed - framerate -> sample_rate
    '''
    Generate a sine wave at a given frequency of five times its time period
    '''
    #sample_rate = 50*max(frequency0,frequency1)
    num_samples = 50
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    #previously - 
    #lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%num_samples)/float(sample_rate))) for i in xrange(num_samples)]
    #print lookup_table[1]
    '''for i in range(4):
        for j in range(num_samples):
            lookup_table.append(lookup_table[j])
            '''
       
    time_period = 1.0/min(frequency0,frequency1)
    start = 0.0
    step  = 1.0/(max(frequency0, frequency1)*num_samples)
    print step
    time = []
    while(start<(5*time_period)):
        if start > (5*time_period):
            start = (5*time_period)
        time.append(start)
        start = start + step      
    
    print len(time)
    lookup_table0 = [float(amplitude) * math.sin(2.0*math.pi*float(frequency0)*time[i]) for i in xrange(len(time))]
    lookup_table1 = [float(amplitude) * math.sin(2.0*math.pi*float(frequency1)*time[i]) for i in xrange(len(time))]
    plt.subplot(211,axisbg='black')
    plt.axis([0,5*time_period,(-(amplitude)-0.5),(amplitude+0.5)])
    plt.plot(time, lookup_table0, 'go')
    plt.plot(time, lookup_table0, 'g')
    plt.ylabel('Amplitude');
    plt.xlabel('Time');
    plt.title('Carrier Waveform');
    plt.text((time_period), amplitude+0.3, 'Frequency = '+str(frequency0) + 'Hz', color = 'red')
    plt.text((time_period), amplitude+0.1, 'Amplitude = '+str(amplitude) + 'units', color = 'red')
    plt.text((3*time_period), amplitude+0.3, 'Time period = '+str(1.0/frequency0) + 's', color = 'red')  
    
    plt.subplot(212,axisbg='black')
    plt.axis([0,5*time_period,(-(amplitude)-0.5),(amplitude+0.5)])
    plt.plot(time, lookup_table1, 'go')
    plt.plot(time, lookup_table1, 'g')
    plt.ylabel('Amplitude');
    plt.xlabel('Time');
    plt.title('Carrier Waveform');
    plt.text((time_period), amplitude+0.3, 'Frequency = '+str(frequency1) + 'Hz', color = 'red')
    plt.text((time_period), amplitude+0.1, 'Amplitude = '+str(amplitude) + 'units', color = 'red')
    plt.text((3*time_period), amplitude+0.3, 'Time period = '+str(1.0/frequency1) + 's', color = 'red')

    plt.show()  
    #print lookup_table
    return #[lookup_table[i%num_samples] for i in range(num_samples)]#count(0))  #count(firstval = 0, step = 1) - function which can start with a first_value and increment with the step value...infinitely..
                                                        # use range fn for finite repetition

f = open('test_file.txt', 'w')
print f
#f.write("Audio Networking using ultrasound")            #Write into Text file
file_input = str(raw_input("Enter data to be written to file: "))
f.write(file_input)            #Write into Text file
f = open('test_file.txt', 'r+')  #Open file for Read & Write
file_content = f.read()          #Read from Text file
print 'Contents of text file :',file_content
len_file = len(file_content)
#print abcd[0]
change = str(raw_input("Do you want to change the default frequency settings(Y)? "))
if change == 'Y':
    f0 = str(raw_input("Enter frequency of bit 0 transmission: "))
    for i in range(len(f0)):
        if (ord(f0[i]) >= 48 and ord(f0[i]) <= 57):
            bool_valid0 = True
        else:
            bool_valid0 = False
            print 'Invalid Input: Enter numeric value only'
            break
    if bool_valid0 == True:
        Freq0 = int(f0)
    else:
        print ""
        #exit program
        
    f1 = str(raw_input("Enter frequency of bit 1 transmission: "))        
    for i in range(len(f1)):
        if (ord(f1[i]) >= 48 and ord(f1[i]) <= 57):
            bool_valid1 = True
        else:
            bool_valid1 = False
            print 'Invalid Input: Enter numeric value only'
            break
    if bool_valid1 == True:
        Freq1 = int(f1)
    else:
        print ''#exit program                                                                            
else:           
    Freq0 = 1000
    Freq1 = 5000

#plt.subplot(211,axisbg='black')
sine_wave(Freq0, Freq1)
#plt.subplot(212,axisbg='black')
#sine_wave(Freq1)
time_period_plot = 1.0/max(Freq0,Freq1)
start = 0.0
num_values = 20
step = time_period_plot/num_values
#print step
time_plot = []
while(start<time_period_plot):
    time_plot.append(start)
    start = start + step 
duration = 500
ascii_values = [ord(c) for c in file_content]
#print ascii_values
binary_values = []
#len_ascii = len(values)
for i in range(len_file):
    temp = bin(ascii_values[i])[2:]
    len_temp = len(temp)
    if (len_temp < 8):
        for j in range(8-len_temp):
            temp = '0' + temp
        binary_values.append(temp)
      
len_bv = len(binary_values);
message_table = []
file_content_encoded_table = []
num_samples = 50      
amplitude = 0.5
if (len_bv == len_file):
    print 'Check'
else:
    print 'False'
#print len_bv
for j in range(len_bv):
    for k in range(8):
        if (binary_values[j][k] == '1'):
            winsound.Beep(Freq1,duration)
            file_content_encoded_table.append(1)
            for i in range(num_samples):
                message_table.append(amplitude) 
        else:
            if(binary_values[j][k] == '0'):
                winsound.Beep(Freq0,duration)
                file_content_encoded_table.append(0)
                for i in range(num_samples):
                    message_table.append(-1*amplitude)

time_message = []
freq_message = 10**3.0/duration
time_period_message = 1/freq_message
start = 0.0
step = time_period_message/num_samples
for i in range(len_bv * 8 * num_samples):
        time_message.append(start)
        start = start + step      

plt.figure()
plt.subplot(111,axisbg='black')
plt.axis([0,max(time_message),(-(amplitude)-0.5),(amplitude+0.5)])
plt.plot(time_message, message_table, 'go')
plt.plot(time_message, message_table, 'g')
plt.ylabel('Amplitude');
plt.xlabel('Time');
plt.title('Message Waveform');
plt.text((time_period_message), amplitude+0.3, 'Frequency = '+str(freq_message) + 'Hz', color = 'red')
plt.text((time_period_message), amplitude+0.1, 'Amplitude = '+str(amplitude) + 'units', color = 'red')
plt.text((2.0*max(time_message)/3), amplitude+0.3, 'Time period = '+str(time_period_message) + 's', color = 'red')
plt.show()                

'''
num_cycles_fsk = time_period_message/time_period_plot
fsk_table = []
time_plot_range = []#list(range(0,max(time_message),step))
start = 0.0
while(start < max(time_message)):
    time_plot_range.append(start)
    start = start + step

for k in range(len(message_table)):
    if message_table[k] == -0.5:
        for i in range(int(num_cycles_fsk)):
            for j in range(len(time_plot)):
                fsk_table.append(float(amplitude) * math.sin(2.0*math.pi*float(Freq0)*time_plot[j])) 
    elif message_table[k] == 0.5:
        for i in range(int(num_cycles_fsk)):
            for j in range(len(time_plot)):
                fsk_table.append(float(amplitude) * math.sin(2.0*math.pi*float(Freq1)*time_plot[j]))
   
plt.subplot(414,axisbg='black')
plt.axis([0,max(time_message),(-(amplitude)-0.5),(amplitude+0.5)])
plt.plot(time_plot_range, fsk_table, 'go')
plt.plot(time_plot_range, fsk_table, 'g')
plt.ylabel('Amplitude');
plt.xlabel('Time');
plt.title('Modulated Waveform');
plt.text((time_period_message), amplitude+0.3, 'Frequency = '+str(freq_message) + 'Hz', color = 'red')
plt.text((time_period_message), amplitude+0.1, 'Amplitude = '+str(amplitude) + 'units', color = 'red')
plt.text((2.0*max(time_message)/3), amplitude+0.3, 'Time period = '+str(time_period_message) + 's', color = 'red')
plt.show()                
'''
#winsound.Beep(10000,duration)
#print (bin(values[4])[2:])
f.close()
#f1.close()
#time.sleep(2) #2 seconds time delay