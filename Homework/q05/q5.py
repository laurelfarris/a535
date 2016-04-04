'''
Programmer:       Laurel Farris
Last modified:    12 February 2016
Instructions:     See q5.pdf for details
Notes:            A separate module with the functions needs to be
                   created, which can then be called in individual
                   homework assignments.
'''

import numpy as np
import math
import pdb
from astropy import constants as const

import conversions


''' Wavelength (Angstroms) '''
wave1 = 3000.0
wave2 = 5500.0
wave3 = 8000.0

'''Part 1: determine the frequency and energy at 5500 Angstroms.'''

frequency = conversions.WaveToFreq(wave2*1e-8)
print "The frequency corresponding to 5500 Angstroms is:", frequency, "Hz."
energy = conversions.WaveToEnergy(wave2*1e-8)
print "The energy corresponding to 5500 Angstroms is:", energy, "erg."

''' Part 2: Determine the conversion factor between F_lambda and F_freq
# at 3000, 5500, and 8000 Angstroms.'''

test_flux = 1.e7 # test flux in erg/s/cm^2
print "1.", test_flux/(conversions.convert_flux(test_flux,wave1*1e-8))
print "2.", test_flux/(conversions.convert_flux(test_flux,wave2*1e-8))
print "3.", test_flux/(conversions.convert_flux(test_flux,wave3*1e-8))

