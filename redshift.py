import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import readcol
import scipy.interpolate
from scipy import  interpolate


files1 = readcol.readcol('60352986.fits.txt' )
files2= readcol.readcol('times.list')


time1= files1[:,0]
time2= files2[:,0]
redshift2= files2[:,1]


result= interpolate.interp1d( redshift2, time2)
#time= np.linspace(0, len(time1))

redshift1= result(time1)

plt.plot(time1, redshift1)
plt.savefig(filename= 'redshift1'+'.png')
plt.plot(time2, redshift2)
plt.savefig(filename= 'redshift2'+'.png')

plt.show()






