'''
Programmer:     Laurel Farris
Description:    Process images for the DIS instrment on the 3.5-m on APO
                (For standard star, at least). Must include wavelength calibration.
Last modified:  5/11/16
'''

import numpy as np
from astropy.io import fits
from pyds9 import *
import glob

''' Functions '''

def full_calib(path)
    ''' 
    User enteres path to fits files. Individual functions below perform
    each calibration step, and the final data, ready for analysis, is returned
    '''
    def read_fits(path):
        ''' input path to fits, output array with data/header '''
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

    def wavelength_calib():
        return 0

    def flux_calib():
        return 0

    def object_red(background_spectrum, data):
        return 0

    path = '/home/holtz/raw/apo/mar16/UT160327/'
    data = read_fits(path).data
    bias_corrected = bias_subtract(bias_list, overscan_subtract(data,10,1065,1037,1072))
    flat_corrected = flat_correct(flat_list, bias_corrected)
    wavelength_calibrated = wavelegnth_calib(lamps, flat_corrected)
    flux_calibrated = flux_calib(flux_list, wavelength_calibrated)
    object_reduced = object_red(spectrum, flux_calibrated)

