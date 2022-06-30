import sys
import wave
import math
import struct
import random
import matplotlib.pyplot as plt
import argparse
from itertools import *
#infinite genration of samples
"""def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5):
    if amplitude > 1.0: amplitude = 1.0
    elif amplitude < 0.0: amplitude = 0.0
    return (float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(1)/float(framerate))) for i in count(0))
    #print amplitude
    """
    
def sine_wave(frequency=400.0, sample_rate=44100, amplitude=0.5):        #changed - framerate -> sample_rate
    '''
    Generate a sine wave at a given frequency of infinite length.
    '''
    period = int(sample_rate / frequency)
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(sample_rate))) for i in xrange(period)]
    #print lookup_table[1]
    plt.subplot(111,axisbg='black')
    plt.plot(lookup_table, 'go')
    plt.plot(lookup_table, 'g')
    #return (lookup_table[i%period] for i in range(0,5*period))#count(0))  #count(firstval = 0, step = 1) - function which can start with a first_value and increment with the step value...infinitely..
                                                        # use range fn for finite repetition
    
def white_noise(amplitude=0.5):
    return (float(amplitude) * random.uniform(-1, 1) for _ in count(0))
    
noise = cycle(islice(white_noise(), 44100))

channels = ((sine_wave(440.0),),(sine_wave(440.0),))                        
channels = ((sine_wave(440.0, amplitude=0.5),),(sine_wave(440.0, amplitude=0.2),))

channels = ((sine_wave(200.0, amplitude=0.1), white_noise(amplitude=0.001)),(sine_wave(205.0, amplitude=0.1), white_noise(amplitude=0.001)))


def compute_samples(channels, nsamples=None):
    return islice(izip(*(imap(sum, izip(*channel)) for channel in channels)), nsamples)
