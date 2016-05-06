'''
Programmer:     Laurel Farris
Description:    Process images for the DIS instrment on the 3.5-m on APO
                (For standard star, at least)
Last modified:  4/29/16
'''

import numpy as np
from astropy.io import fits
from pyds9 import *
import glob

''' Functions '''

def read_fits(path):
    ''' input path to fits, output array with data/header '''
    fls = glob.glob(path)
    hdu=[]
    for f in fls:
        hdu.append(fits.open(f)[0])
    return hdu


