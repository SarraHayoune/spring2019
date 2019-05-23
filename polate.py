from scipy import interpolate
import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import readcol



files = readcol.readcol('/mnt/h229/files.list')
files = files[:,0]

# function to find black hole
def findBH(s):
    #BHfilter = pynbody.filt.LowPass('tform',0.0)
    BHfilter = np.where(s.stars['iord']== 60352986)

    BH = s.stars[BHfilter]
    return BH

#function to find the halos that the galaxy is in
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

#using the function the halos

def getz(s):
    return s.properties['z']
def gettime(s):
    return pynbody.analysis.cosmology.age(s)

f= open("ruthbh.dat","w+")
for i in range (6,60):
    #file= files[6]
    # loading the snapshotS
    s=pynbody.load('/mnt/h229/'+files[i])
    # convert the units 
    s.physical_units()
    #  load any available halo
    h = s.halos()
    BH = findBH(s)
    BHhalos = findBHhalos(s)
    #sorting the halos, indexes/indecis are like an exact address
    currenthalo = np.argsort(BHhalos)
    print BHhalos[currenthalo]


    #which halo are we on?
    currenthalo = BHhalos[0]
    print 'current halo: ', currenthalo
     #this is the position of black hole
    BHposition=BH['pos']

    #putting the x-values into a column
    BHx= BHposition[[i],0]
    print "x postion", BHx
   
    #putting the y-values into a column
    BHy= BHposition[[i],1]
    print "y position", BHy

    #putting the z-values into a column
    BHz= BHposition[[i],2]
    print "z position", BHz 
    
   
    
   # p=pynbody.analysis.halo.center_of_mass(h[currenthalo])
   # print p

   # data = [currenthalo, gettime(s),p ]
   
        
        
    data= str(data)
    data= data[1:-1]
    f.write(data+'\n')
    print data
         
f.close()

   
