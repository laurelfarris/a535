'''
This code takes as input the apparent magnitude of each of two stars,
and computes and returns the apparent magnitude of the two stars
combined. The reference flux is the flux of Vega at 5500 Angstroms
[erg/s/cm^2/Angstrom].
'''
import math

F_ref = 3.60e-9 # Reference flux
def combine_magnitudes(m1,m2):
    F1 = 10.0**(-m1/2.5)*F_ref
    F2 = 10.0**(-m2/2.5)*F_ref
    return -2.5*math.log10((F1+F2)/F_ref)

'''
 Calculate combined magnitude for two stars with individual
 magnitudes m1=17 and m2=18.
'''
print combine_magnitudes(17,18)
