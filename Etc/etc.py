'''
Atmospheric transmission, a (extinction, refraction, etc.)
System effeciency, q
Telescope throughput
Instrument throughput
Filter throughput
Grating specification
'''

import numpy as np
import math
from astropy import constants as const

''' Define constants '''
c = const.c.cgs.value
h = const.h.cgs.value

def atm_transmission(bandpass, object_mag, airmass)
    '''
    Calculate the atmospheric transmission (a),
    which should be between 0 and 1
    (fraction of total light from oject that made it through the atmosphere).

      ``the amount of light lost [magnitudes] can be specified by a
        set of extinction coefficients''.

    net_mag is the magnitude at the bottom of the atmosphere,
    k is the (POSITIVE) extinction coefficient, to be read in from a file
    using the bandpass information (still need to figure out how to do this).
    '''
    f = open('extinction.txt')
    wavelength,k = np.loadtxt(f, unpack=True)

    ''' Math (not to be used in actual code) '''
    net_mag = object_mag + k*airmass
    net_mag - object_mag = -2.5*math.log10(net_flux/object_flux)
    net_mag - object_mag = -2.5*math.log10(a)
    a = 10.^((net_mag - object_mag)/-2.5)
    a = 10.^((k*airmass)/-2.5)

    ''' Value to be returned in code '''
    return 10.^(k*airmass / -2.5)

def sys_transmission(wavelength):
    '''
    Calculate the system transmission (q), using the telescope
    throughput, filter throughput, and detector efficiency; all three of
    which are calculated within their own function embedded below.
    '''
    def telescope_throughput():
        return 0
    def filter_throughput():
        return 0
    def detector_efficiency():
        return 0
    return q


