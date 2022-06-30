import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

#'''
CHUNK = 1024 #1024 #change to 2048 ?
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 1 #2 
RATE = 44100 #sample rate
RECORD_SECONDS = 26
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
#''' 

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
        freq0 = int(f0)
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
        freq1 = int(f1)
    else:
        print ''#exit program                                                                            
else:           
    freq0 = 1000
    freq1 = 5000
chunk = 22050
num_samples = 0
delta = 10
#freq0 = 1000
#freq1 = 5000
bits = ''
bit_count = 0
ascii = 0
file_content = ''

# open up a wave
wf = wave.open('output.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)

# read some data
#print("2")
data = wf.readframes(chunk)
print len(data)
print (chunk*swidth)
bit_list = []
num_values = 50
amplitude = 0.5
message_table = []
# play stream and find the frequency of each chunk
while len(data) == chunk*swidth:
    # write data out to the audio stream
    stream.write(data)
    #print("1")
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                        data))*window
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        
        if ((thefreq >= (freq1-delta)) and (thefreq <= (freq1+delta))):
            bits = bits + str(1)
            bit_list.append(1)
            print "The freq is %f Hz." % (thefreq)
            for i in range(num_values):
                message_table.append(amplitude) 
        elif ((thefreq >= (freq0-delta)) and (thefreq <= (freq0+delta))):
            bits = bits + str(0)
            bit_list.append(0)            
            print "The freq is %f Hz." % (thefreq)
            for i in range(num_values):
                message_table.append(-1*amplitude)
        bit_count = len(bits)
        if bit_count != 0:
            ascii = ascii + int(bits[bit_count-1])*2**(8-bit_count)
        num_samples += 1
        if bit_count == 8:
            #print ascii
            file_content += str(unichr(ascii))
            bits = ''
            ascii = 0
        #if ((thefreq >= (10000-delta)) and (thefreq <= (10000+delta))):
        #    break            
                            
    else:
        thefreq = which*RATE/chunk
        
        if ((thefreq >= (freq1-delta)) and (thefreq <= (freq1+delta))):
            bits = bits + str(1)
            bit_list.append(1)
            print "The freq is %f Hz." % (thefreq)
            for i in range(num_values):
                message_table.append(amplitude) 
            print "The freq is %f Hz." % (thefreq)
        elif ((thefreq >= (freq0-delta)) and (thefreq <= (freq0+delta))):
            bits = bits + str(0)
            bit_list.append(0)            
            print "The freq is %f Hz." % (thefreq)
            for i in range(num_values):
                message_table.append(-1*amplitude)
            print "The freq is %f Hz." % (thefreq)
        bit_count = len(bits)
        if bit_count != 0:
            ascii = ascii + int(bits[bit_count-1])*2**(8-bit_count)
        if bit_count == 8:
            #print ascii
            file_content += str(unichr(ascii))
            bits = ''
            ascii = 0
        #num_samples += 1
        #if ((thefreq >= (10000-delta)) and (thefreq <= (10000+delta))):
        #    break            
    # read some more data
    data = wf.readframes(chunk)
if data:
    stream.write(data)
#print (num_samples*2048)
#print swidth
stream.close()
p.terminate()
print file_content

time_message = []
freq_message = RATE/chunk
time_period_message = 1.0/freq_message
start = 0.0
step = time_period_message/num_values
for i in range(len(message_table)):
        time_message.append(start)
        start = start + step      

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
if ((frequency >= (freq1-delta)) and (frequency <= (freq1+delta))):
    bits = bits + str(1)
elif ((frequency >= (freq0-delta)) and (frequency <= (freq0+delta))):
    bits = bits + str(0)
bit_count = len(bits)
ascii = ascii + int(bits[bit_count-1])*2**(8-bit_count)
'''                    