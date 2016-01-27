# Programmer:       Laurel Farris
# Last modified:    27 January 2016
# Instructions:     See q5.pdf for details
# Notes:            A separate module with the functions needs to be
#                   created, which can then be called in individual
#                   homework assignments.

import numpy as np
import math
import pdb
from astropy import constants as const

# Constants needed for conversion [cgs]
c = const.c.cgs.value # speed of light
h = const.h.cgs.value # Plank's constant

# Functions for converting between wavelength, frequency, and energy,
# INPUT wavelengths must be in cgs units [cm], but OUTPUT wavelengths
# are in Angstroms.
def WaveToFreq(wave):
    return c/wave
def FreqToWave(freq):
    return (c/freq)*1e8
def EnergyToWave(energy):
    return (h*c)/energy*1e8
def WaveToEnergy(wave):
    return (h*c)/wave
def EnergyToFreq(energy):
    return energy/h
def FreqToEnergy(freq):
    return h*freq

# Convert between F_lambda and F_nu,
# given a wavelength (or frequency), both in cgs,
# and the flux at that wavelength/frequency.
def convert_flux(flux, something):
    return flux*(something**2)/c

# Convert from the STMAG system to the ABNU system
def STMAG_to_ABNU(m_STMAG, wave):
    return m_STMAG - 2.5*math.log10(wave**2/c) - 27.5
def ABNU_to_STMAG(m_ABNU, freq):
    return m_ABNU - 2.5*math.log10(c/freq**2) + 27.5





