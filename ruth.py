import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import readcol
import scipy.interpolate
from scipy import  interpolate

# Read data from files
files1 = readcol.readcol('60352986.fits.txt' )
files2 = readcol.readcol('60354630.fits.txt')
files3 = readcol.readcol('Ruth.dat')

time1= files1[:,0]
time2= files2[:,0]
time3= files3[:,1]
x1 = files1[:,1]
x2 = files2[:,1]
y1 = files1[:,2]
y2 = files2[:,2]
z1 = files1[:,3]
z2 = files2[:,3]
x  = files3[:,2]
y  = files3[:,3]
z  = files3[:,4]

# interpolate for BH1 '60352986' and BH2 '60354630'
result1= interpolate.interp1d(x, time3)
x1_position= result1(time1)
x2_position= result1(time2)

result2= interpolate.interp1d(y, time3)
y1_position= result2(time1)
y2_position= result2(time2)


result3= interpolate.interp1d(z, time3)
z1_position= result3(time2)
z2_position= result3(time2)


new_x1_position = np.subtract(x1, x1_position)
new_y1_position = np.subtract(y1, y1_position)

new_x2_position = np.subtract(x2, x2_position)
new_y2_position = np.subtract(y2, y2_position)


# plot the resulting BH1 x vs y   and BH2  x vs y  with their new positions
plt.plot(new_x1_position, new_y1_position )
plt.plot(new_x2_position, new_y2_position )

plt.savefig(filename= 'new_position'+'.png')

plt.show()





