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

# interpolate for BH1 '60352986'
result11= interpolate.interp1d(x, time3)
x1_position= result11(time1)

result12= interpolate.interp1d(y, time3)
y1_position= result12(time1)

result13= interpolate.interp1d(z, time3)
z1_position= result13(time1)

#interpolate for BH2 '60354630'
result21= interpolate.interp1d(x, time3)
x1_position= result1(time1)

result22= interpolate.interp1d(y, time3)
y1_position= result2(time1)

result23= interpolate.interp1d(z, time3)
z1_position= result3(time1)



new_x_position = np.subtract(x1, x_position)
new_y_position = np.subtract(y1, y_position)


#plt.plot(time1, redshift1)
plt.savefig(filename= 'redshift1'+'.png')
plt.plot(time2, redshift2)
plt.savefig(filename= 'redshift2'+'.png')

plt.show()





