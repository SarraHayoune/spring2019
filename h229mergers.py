import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import readcol


files = readcol.readcol('/Jillian/h229/files.list')
files = files[:,0]
def getz(s):
    return s.properties['z']
    
f =  open("h229.dat", "w+") 
for file in files:
    
    # loading the snapshotS
    s =pynbody.load('/Jillian/h229/'+file)
    print s
    data = [getz(s)] 
        
        
    data= str(data)
    data= data[1:-1]
    f.write(data+'\n')
    
print data
         
f.close()
