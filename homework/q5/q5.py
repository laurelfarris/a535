# Instructions:
    # Write functions that convert between
    # wavelength, frequency, and energy;
    # and between F_lambda and F_nu, using Angstroms and Hertz.
    #
    # Using the functions, determine the frequency and energy at
    # 5500 Angstroms, as well as the conversion factor between
    # Flux_lambda and Flux_frequency at 3000, 5500, and 8000 Angstroms.


import numpy as np
import math
import pdb
from astropy import constants as const

# Constants needed for conversion [cgs]
c = const.c.cgs.value # speed of light
h = const.h.cgs.value # Plank's constant

# Functions for converting between wavelength, frequency, and energy

def WaveToFreq(wave):
    return c/wave

def FreqToWave(freq):
    return c/freq

def EnergyToWave(energy):
    return (h*c)/energy

def WaveToEnergy(wave):
    return (h*c)/wave

def EnergyToFreq(energy):
    return energy/h

def FreqToEnergy(freq):
    return h*freq

# Functions for converting between Flux as a function of frequency and
# of wavelength

def Flux_FreqToWave:
    return 0

def Flux_WaveToFreq:
    return 0

wave1 = 3000.0
wave2 = 5500.0
wave3 = 8000.0

freq = WaveToFreq(21.0)
print freq

