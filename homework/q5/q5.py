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

# Functions for converting between Flux as a function of frequency and
# of wavelength (not completed yet).

def Flux_FreqToWave(freq,F_freq):
    return -F_freq(freq**2/c)

def Flux_WaveToFreq(wave,F_wave):
    return -F_wave(wave**2/c)

## Homework (need to review syntax for python output formatting).

wave1 = 3000.0
wave2 = 5500.0
wave3 = 8000.0

# Problem 1: determine the frequency and energy at 5500 Angstroms.
frequency = WaveToFreq(wave2*1e-8)
print "The frequency of a 5500 Angstrom wave is:", frequency, "Hz."
energy = WaveToEnergy(wave2*1e-8)
print "The energy of a 5500 Angstrom wave is:", energy, "erg."




