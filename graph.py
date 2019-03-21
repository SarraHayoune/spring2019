import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('testdata.txt')
Time= files[:,0]
BHmass = files [:,2]
BHDistance= files[:,3]

#plt.plot(Time, BHDistance)
#plt.ylabel('BH Distance')
#plt.xlabel('Time')


plt.xlabel("Time 'Gyr'")
plt.ylabel("BH Mass 'Kpc'")
plt.plot(Time, BHmass,"b-", linewidth=2)
plt.tick_params(axis="BHmass", labelcolor="b")

plt.twinx()
plt.ylabel("BH Distance 'Kpc'")
plt.plot(Time, BHDistance, "r-", linewidth=2)

plt.tick_params(axis="BHdistance", labelcolor="r")

plt.show()
