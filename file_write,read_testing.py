import time
f = open('test_run.txt', 'w')
print f
f.write("This is a test run123   i like this")
f = open('test_run.txt', 'r+')
abcd = f.read()
print abcd
len_str = len(abcd)
print abcd[0]
values = [ord(c) for c in abcd]
print values
len_list = len(values)
print (bin(values[4])[2:])
f.close()
#f1.close()
#time.sleep(2) #2 seconds time delay