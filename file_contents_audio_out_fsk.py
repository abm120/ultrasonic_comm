import time
import winsound

f = open('test_file.txt', 'w')
print f
#f.write("Audio Networking using ultrasound")            #Write into Text file
f.write("Audio")            #Write into Text file
f = open('test_file.txt', 'r+')  #Open file for Read & Write
file_content = f.read()          #Read from Text file
print 'Contents of text file :',file_content
len_file = len(file_content)
#print abcd[0]
Freq0 = 17000
Freq1 = 22000
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
if (len_bv == len_file):
    print 'True'
else:
    print 'False'
#print len_bv
for j in range(len_bv):
    for k in range(8):
        if (binary_values[j][k] == '1'):
            winsound.Beep(Freq1,duration)
        else:
            if(binary_values[j][k] == '0'):
                winsound.Beep(Freq0,duration)


#print (bin(values[4])[2:])
f.close()
#f1.close()
#time.sleep(2) #2 seconds time delay