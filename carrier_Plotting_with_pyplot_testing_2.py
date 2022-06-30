# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.01)
t2 = np.arange(0.0, 0.001, (1.8*(10**-6))) #Sampling frequency = 24 * Carrier Frequency; Inter-sample time = 1.8ú seconds
#t2 = np.arange(0.0, 0.001, (1.976*(10**-6)))


plt.figure(1)
#plt.subplot(211)
#plt.plot(t1, f(t1), 'bo', t1, f(t1), 'k')

#plt.subplot(212)
plt.subplot(111,axisbg='black')
plt.plot(t2, np.cos(2*np.pi*t2*23000), 'go',t2, np.cos(2*np.pi*t2*23000), 'g')
plt.ylabel('Amplitude');
plt.xlabel('Time');
plt.title('Carrier Waveform');
plt.text(1, 0.5, r'$\mu=100,\ \sigma=15$', color = 'red')
plt.show()
