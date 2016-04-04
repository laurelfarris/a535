
import numpy as np
from astropy.io import fits
from pyds9 import *

def readfile(filename):
    return fits.open('/home/holtz/raw/apo/dec06/UT061215/'+filename)[0].data

def bias_sub(image):
    return image-image[10:1065,1037:1072].mean()
 
def norm(image):
    return image/image[400:600,400:600].mean()


def combine(lis):
    '''Jon's stuff'''
    cube=np.array(lis)
    return np.median(cube,axis=0)

def mkflat(files):
    '''Jon's stuff'''
    list=[]
    for file in files:
        im = rd(file)
        list.append(norm(biassub(im)))

a = readfile('SN17135_r.0103.fits')

d = DS9()
d.set_pyfits(a)

f1 = readfile('flat_r.0013.fits')
f2 = readfile('flat_r.0014.fits')
f3 = readfile('flat_r.0015.fits')

n1 = norm(f1)
n2 = norm(f2)
n3 = norm(f3)

nlist = [n1,n2,n3]
