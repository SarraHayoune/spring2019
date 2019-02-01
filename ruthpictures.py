import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_functions as BHF

files = readcol.readcol('/Jillian/h229/files.list')
files = files[:,0]
    
f =  open("h229.dat", "w+") 
for j in range(13)::
    
    # loading the snapshotS
    s =pynbody.load('/Jillian/h229/'+file)
    s.physical_units()
    # convert the units
    s.physical_units()

    # load the halos
    h = s.halos()

    # function to find black hole
    def findBH(s):
        BHfilter = pynbody.filt.LowPass('tform',0.0)
        BH = s.stars[BHfilter]
        return BH

    BH = findBH(s)

    # function to find the halos that the galaxy is in
    def findBHhalos (s):
         BH = findBH(s)
         BHhalos = BH ['amiga.grp']
         return BHhalos


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
    BHx1= BHposition[[1],0]
    BHx2= BHposition[[2],0]
    #print "x postion", BHx
   
        #putting the y-values into a column
    BHy1= BHposition[[1],1]
    BHy2= BHposition[[2],1]
    #print "y positon", BHy

         #putting the z-values into a column
    BHz1= BHposition[[1],2]
    BHz2= BHposition[[2],2]
    #print "z position", BHz
   
    #plt.plot(BHx, BHy,'+') 
    # create an image using  the default bands (i, v, u)
    #pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo'+str(h2)+'.png')
    BHF.render(s,width= '25 kpc', plot= True, ret_im= True, filename='ruthpictures.png')
    plt.plot(BHx1, BHy1,'+')
    plt.plot(BHx2, BHy2,'+')
    plt.savefig('ruthfaceon.png')
