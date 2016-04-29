'''
Programmer:     Laurel Farris
Description:    Process images for the ARCTIC instrment on the 3.5-m on APO
Last modified:  4/28/16
'''

import numpy as np
from astropy.io import fits
from pyds9 import *
import glob


''' Functions '''

def pick_data(day):
    full_date = 'UT1603' + str(day) + '/'
    return '/home/holtz/raw/apo/mar16/' + full_date

def make_cube(fits_list):
    fls = glob.glob(fits_list)
    hdu=[]
    for f in fls:
        hdu.append(fits.open(f)[0])

def bias_red(bias_lis, lis):
   return lis-bias_lis 

def dark_red(dark_lis, lis):
    return lis-dark_lis

def flat_red(flat_lis, lis):
    return lis/flat_lis



''' Pick date and files to use '''
path = pick_data(27)
full_path = path + 'ARCTIC_Bias*.fits'
bias_cube = make_cube(full_path)

''' Set variable for ds9 object '''
#d = DS9()
