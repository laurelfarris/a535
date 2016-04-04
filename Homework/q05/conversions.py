'''
Programmer:       Laurel Farris
Last modified:    27 January 2016
Instructions:     See q5.pdf for details
Notes:            A separate module with the functions needs to be
                   created, which can then be called in individual
                   homework assignments.
'''

import numpy as np
import math
import pdb
from astropy import constants as const

'''
Constants: speed of light and Plank's,
both in cgs units
'''
c = const.c.cgs.value
h = const.h.cgs.value


def WaveToFreq(wave):
    return c/wave

def FreqToWave(freq):
    return (c/freq)*1.e8
    
def EnergyToWave(energy):
    return (h*c)/energy*1.e8

def WaveToEnergy(wave):
    return (h*c)/wave

def EnergyToFreq(energy):
    return energy/h

def FreqToEnergy(freq):
    return h*freq


def convert_flux(flux, something):
    '''
    Convert between F_lambda and F_nu,
    given a wavelength (or frequency), both in cgs,
    and the flux at that wavelength/frequency.
    '''
    return flux*(something**2)/c

def STMAG_to_ABNU(m_STMAG, wave):
    '''
    Convert from the STMAG system to the ABNU system
    '''
    return m_STMAG - 2.5*math.log10(wave**2/c) - 27.5

def ABNU_to_STMAG(m_ABNU, freq):
    '''
    Convert from the ABNU system to the STMAG system
    '''
    return m_ABNU - 2.5*math.log10(c/freq**2) + 27.5





