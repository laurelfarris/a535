'''
Programmer:     Laurel Farris
Description:    This program contains the initial developments of an
                exposure time calculator to be used for the APO 3.5m.
                Given known values, such as the diameter of a
                telescope in meters, the program will eventually use
                these values to calculate the amount of time that an
                object should be observed.
                Possibly input RA and Dec, time of year, etc. to
                determine these values?
                Maybe set up similiar to the isochrone assignment from
                last semester, where different values can be
                specified, and a default (such as a = 0.9) is
                returned?
'''

import math
from astropy import constants as const

'''
Define constants
'''
c = const.c.cgs.value
h = const.h.cgs.value

def photon_flux(magnitude,wavelength):
    '''
    Calculate the photon flux, S' (number of photons per second per square
    cm) given the values returned by each of the functions defined
    below.
    '''


def telescope_area(size,wavelength):
    '''
    Calculate the area [cm^-2] of the telescope.
    '''
    return math.pi*((size*100.)/2.)**2


def atm_transmission(wavelength):
    '''
    Calculate the atmospheric transmission (a) given...?
    Haziness/transparency, seeing, airmass, etc.
    '''


def sys_transmission(wavelength):
    '''
    Calculate the system transmission (q), using the telescope
    throughput, filter throughput, and detector efficiency; all three of
    which are calculated within their own function embedded below. 
    '''
    def telescope_throughput():
    def filter_throughput():
    def detector_efficiency():



