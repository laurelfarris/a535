'''
Programmer:     Laurel Farris
Description:    Process images for the ARCTIC instrment on the 3.5-m on APO
                (For standard star, at least)
Last modified:  4/29/16
'''

import numpy as np
from astropy.io import fits
from pyds9 import *
import glob


''' Functions '''

def read_fits(path):
    ''' input path to fits, output array with data/heaer '''
    fls = glob.glob(path)
    hdu=[]
    for f in fls:
        hdu.append(fits.open(f)[0])
    return hdu

def overscan_subtract(frames, x1,x2,y1,y2):
    os = []
    for f in frames:
        os.append( f.data-(f.data[x1:x2,y1:y2].mean()) )
    return os

def bias_subtract(bias_lis, lis):
   return lis-bias_lis 

def flat_correct(flat_lis, lis):
    return lis/flat_lis


''' Test for March 27, 2016 (UT) '''
# Look at log and manually make list of each type of image
path = '/home/holtz/raw/apo/mar16/UT160327/'
bias_frames = read_fits(path + 'ARCTIC_Bias*.fits')
oc_bias = overscan_subtract(bias_frames, 10,1065,1037,1072)
#bias_cube = data_cube(full_path) 

''' testing '''
#im = read_fits('/home/holtz/raw/apo/dec06/UT061215/SN17135_r.0103.fits')[0].data
#im2 = overscan_sub(im,10,1065,1037,1072)
#im3 = bias_red(im2)

