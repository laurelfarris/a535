'''
Programmer:     Laurel Farris
Description:    This program takes the apparent V magnitude
                of a star, along with the telescope size and
                detector efficiency, and determines the number of photons
                received per second.
'''

import math
from astropy import constants as const

'''
Define constants
'''
c = const.c.cgs.value
h = const.h.cgs.value

def mag_to_flux(mag, F_ref):
    '''
    Given an object's apparent V mag and a reference flux,
    calculate the object's flux.
    '''
    return 10.0**(mag/(-2.5))*F_ref

def S_prime(F_lambda,q,a,wave_lower,wave_upper):
    '''
    Return the photon rate [photons per second per cm^2]
    '''
    return (F_lambda*q*a/(2.*h*c))*(wave_upper**2-wave_lower)

F_Vega = 3.6e-9
Vmag = 22.
a = 1.
q = .5
diameter = 100.

flux = mag_to_flux(Vmag, F_Vega)
T = math.pi*(diameter/2)**2
S = S_prime(flux,0.5,1.,5000.,6000.)

count = T*S
print '{:.2e} photons per second'.format(count)
