'''
Atmospheric transmission, a (extinction, refraction, etc.)
System effeciency, q
Telescope throughput
Instrument throughput
Filter throughput
Grating specification
'''

import math
from astropy import constants as const

''' Define constants '''
c = const.c.cgs.value
h = const.h.cgs.value

def atm_transmission(wavelength, seeing, airmass, moon):
    '''
    Calculate the atmospheric transmission (a)
    Haziness/transparency, seeing, airmass, etc.
    '''
    k = -1.086*tau
    a = ...
    return a

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

