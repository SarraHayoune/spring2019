# making a graph of the position of two black holes

import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import readcol


files1 = readcol.readcol('60352986.fits.txt' )
files2 = readcol.readcol('60354630.fits.txt' )
# limit the time for one black hole, we are interested in the period until the merge happen not after

maxtime=max(files2[:,0])
print maxtime

index= np.where(files1[:,0] <= maxtime)

# set the x & y positions from black holes files
x_position1= files1[:,1]
x_position= x_position1[index]

y_position1= files1[:,1]
y_position= y_position1[index]


X_POSITION2 = files2[:,1]
Y_POSITION2= files2[:,2]
#Y_POSITION= np.array(Y_POSITION)
# plotting x & y positions of both black holes in one graph
plt.plot(x_position, y_position)
plt.ylabel("Y-POSITION for 60352986 " )
plt.xlabel("X-POSITION")

plt.tick_params(axis="Y-POSITION for 60354630", labelcolor= "b")

plt.plot(X_POSITION2,Y_POSITION2)
plt.twinx()
plt.ylabel("Y-POSITION for 60354630")

#plt.plot(X_POSITION1,Y_POSITION1)
plt.tick_params(axis="Y-POSITION for 60352986", labelcolor= "r")


plt.savefig(filename= 'pplot1'+'.png')

plt.show()
