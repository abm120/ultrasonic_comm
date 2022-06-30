# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
#import recording_sound.py

chunk = 22050
num_samples = 0
delta = 10
freq0 = 14000
freq1 = 16000
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
            print "The freq is %f Hz." % (thefreq)
        elif ((thefreq >= (freq0-delta)) and (thefreq <= (freq0+delta))):
            bits = bits + str(0)
            print "The freq is %f Hz." % (thefreq)
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
            print "The freq is %f Hz." % (thefreq)
        elif ((thefreq >= (freq0-delta)) and (thefreq <= (freq0+delta))):
            bits = bits + str(0)
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



'''
if ((frequency >= (freq1-delta)) and (frequency <= (freq1+delta))):
    bits = bits + str(1)
elif ((frequency >= (freq0-delta)) and (frequency <= (freq0+delta))):
    bits = bits + str(0)
bit_count = len(bits)
ascii = ascii + int(bits[bit_count-1])*2**(8-bit_count)
'''                    