import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_FUNCTIONS.py as BHF


# load the snapshot and set to physical units

#s= pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')
s= pynbody.load('/jillian/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')


# convert the units
s.physical_units()

 # load the halos
h = s.halos()

 # function to find black hole
def findBH(S):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)

# function to find the halos that the galaxy is in
def findBHhalos (s):
    BH = findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos


BHhalos = findBHhalos(s)

 #sorting the halos, indexes/indecis are like an exact address
halolist = np.argsort(BHhalos)
#print BHhalos[currenthalo]



for i in halolist:
    
        #which halo are we on?
    currenthalo = BHhalos[i]
    print 'current halo: ', currenthalo
    print i
    

 # center on the largest halo and aligh the disk
      
    pynbody.analysis.halo.center(h[currenthalo], mode= 'hyb')
        
       

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
    
    # create an image using  the default bands (i, v, u)
    #plt.plot(BHx, BHy,'+') 
    BHF.render(s,width= '15 kpc',plot=True,ret_im=True,filename='halo'+str(currenthalo)+'.png')
    plt.plot(BHx, BHy,'+')
                        
    #plot_BH_pos(h[currenthalo].s, BH,'tform', w=20, save=True)
