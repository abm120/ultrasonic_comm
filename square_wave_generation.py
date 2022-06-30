import sys
import wave
import math
import struct
import random
import argparse
import matplotlib.pyplot as plt
from itertools import *

def square_wave(frequency=5000.0, sample_rate=44100, amplitude=0.5):        #changed - framerate -> sample_rate
    '''
    Generate a sine wave at a given frequency of five times its time period
    '''
    sample_rate = 50*frequency
    num_samples = int(sample_rate / frequency)
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    lookup_table = [float(amplitude) * (-1)**(math.floor(2*i/num_samples)) for i in xrange(num_samples)]
    #print lookup_table[1]
    for i in range(4):
        for j in range(num_samples):
            lookup_table.append(lookup_table[j])
       
    time_period = 1.0/frequency
    start = 0.0
    step  = time_period/num_samples
    print step
    time = []
    for i in range(5*num_samples):
        if start > (5*time_period):
            start = (5*time_period)
        time.append(start)
        start = start + step      
              
    plt.subplot(111,axisbg='black')
    plt.axis([0,5*time_period,(-(amplitude)-0.5),(amplitude+0.5)])
    plt.plot(time, lookup_table, 'go')
    plt.plot(time, lookup_table, 'g')
    plt.ylabel('Amplitude');
    plt.xlabel('Time');
    plt.title('Carrier Waveform');
    plt.text((time_period), amplitude+0.3, 'Frequency = '+str(frequency) + 'Hz', color = 'red')
    plt.text((time_period), amplitude+0.2, 'Amplitude = '+str(amplitude) + 'units', color = 'red')
    plt.text((2*time_period), amplitude+0.3, 'Time period = '+str(time_period) + 's', color = 'red')    
    plt.show()
    #print lookup_table
    return [lookup_table[i%num_samples] for i in range(num_samples)]#count(0))  #count(firstval = 0, step = 1) - function which can start with a first_value and increment with the step value...infinitely..
                                                        # use range fn for finite repetition