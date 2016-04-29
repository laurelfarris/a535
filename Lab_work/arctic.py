'''
Programmer:     Laurel Farris
Description:    Process images for the ARCTIC instrment on the 3.5-m on APO
Last modified:  4/28/16
'''

import numpy as np
from astropy.io import fits
from pyds9 import *


''' Set variable for ds9 object '''
d = DS9()
d.set_pyfits(a)

''' Create cube of header/data stuff '''
fls = readfile(glob.glob('/home/holtz/raw/apo/mar16/UT160327/*.fits'))

''' Input filename and return data/header cube'''
hdu=[]
for f in fls:
    hdu.append(fits.open(f)[0])

bias=[]
dark=[]
flat=[]
im=[]
for i in range(0,len(hdu)):
    if hdu[i].header.something == bias:
        bias.append(hdu[i])
    elif hdu[i].header.something == dark:
        dark.append(hdu[i])
    elif hdu[i].header.something == flat:
        dark.append(hdu[i])
    else hdu[i].header.something == image:
        dark.append(hdu[i])




''' bias subtraction (based on overscan) '''
bias_sub = image-image[10:1065,1037:1072].mean()

''' Normalize image by dividing by mean background counts '''
# This is the flat correction...?
# Needs to be changed to something more general
norm = image/image[400:600,400:600].mean()

''' Input images to be corrected for flats '''
def flat_correct(hdu):
    flats = []
    for x in hdu:
        flats.append(norm(bias_sub(x)))

''' Normalize the flats '''
n1 = norm(f1)
n2 = norm(f2)
n3 = norm(f3)

nlist = [n1,n2,n3]

''' Read Images '''
a = readfile('SN17135_r.0103.fits')
#fls = readfiles('*.fits')

''' Jon's stuff:
def combine(lis):
    cube=np.array(lis)
    return np.median(cube,axis=0)
'''





