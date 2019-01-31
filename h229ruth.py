
# Assignement4: make the snap loop
import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import readcol

('/jillian/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')
files = readcol.readcol('/Jillian/h229/files.list')
files = files[:,0]

# function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
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

f =  open("h229.dat", "w+") 
for file in files:
    
    # loading the snapshotS
    s =pynbody.load('/Jillian/h229/'+file)
 
    # convert the units 
    s.physical_units()

    #  load any available halo
    h = s.halos()
    BH = findBH(s)
    BHhalos = findBHhalos(s)
    #sorting the halos, indexes/indecis are like an exact address
    currenthalo = np.argsort(BHhalos)
    print BHhalos[currenthalo]

    for i in currenthalo:
    
        #which halo are we on?
        currenthalo = BHhalos[i]
        print 'current halo: ', currenthalo
        print i
    
        #put the galaxy you care about in the center of the simulation
        pynbody.analysis.angmom.faceon(h[currenthalo])

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

        #the .5 is the square root , this is the distance formula
        distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
        print "the distance is:", distance
        
        starmass = h[currenthalo].s['mass'].sum()
        gasmass = h[currenthalo].g['mass'].sum()
        virialmass = starmass+gasmass+h[currenthalo].d['mass'].sum()
    
        data = [currenthalo, BH['iord'][i], gettime(s),getz(s), BH['mass'][i], BH['r'][i], starmass, gasmass, virialmass] 
        
        
        data= str(data)
        data= data[1:-1]
        f.write(data+'\n')
    
    print data
         
f.close()
