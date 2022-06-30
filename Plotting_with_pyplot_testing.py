"""
This is plotting tutorial workout/ practice
"""
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
plt.plot([2,1,6,3],'bo')
plt.plot([2,1,6,3])
plt.plot([1,2,3,4], [1,4,9,16],'ro')
plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
#plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
#plt.plot([1,2,3,4], [1,4,9,16])
#plt.plot([1,2],[2,3],[3,4],[4,5], aa=False)
#plt.plot([1,2],[2,3],[3,4],[4,5], aa=True)
#plt.plot([2,3], [1,2], color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=12)
line, = plt.plot([2,3], [1,2], '-')
line.set_antialiased(False) # turn off antialising
linea, = plt.plot([3,4], [2,3], '-')
linea.set_antialiased(True) # turn on antialising
lines = plt.plot([1,2],[2,3],[3,4],[4,5])


#plt.setp(lines, color='r', linewidth=2.0)
plt.ylabel('Some Numbers')
plt.xlabel('Num Count')
plt.axis([0, 6, 0, 20])
plt.legend()
plt.show()
#plt.plot(t, t, 'r--', t, t**2, 'ys', t, t**3, 'g^')
#plt.show()