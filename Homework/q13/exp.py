'''
Programmer:     Laurel Farris
Description:    This program will serve as an
                exposure time calculator to be used for the APO 3.5m.
                Given known values, such as the source brightness,
                telescope and instrument information, moon phase, etc.,
                the program will calculate the required exposure time
'''

import math
from astropy import constants as const

''' Define constants '''
c = const.c.cgs.value
h = const.h.cgs.value

def count_equation

''' target input '''
''' instrument configuration input '''
''' observing condition input '''
''' output choices'''



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



