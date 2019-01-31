import pynbody
import matplotlib.pylab as plt


# load the snapshot and set to physical units

s= pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

# convert the units
s.physical_units()

 # load the halos
h = s.halos()



 # center on the largest halo and aligh the disk
pynbody.analysis.angmom.faceon(h[11])

  # create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '10 kpc',plot=True,ret_im=True,filename='halo11Faceon.png')
# center on the largest halo and aligh the disk
pynbody.analysis.angmom.sideon(h[5])

  # create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '10 kpc',plot=True,ret_im=True,filename='halo11edgeon.png')
