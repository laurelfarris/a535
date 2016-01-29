import math
import pdb

# Import 'conversions.py' from question 5
import conversions
 
J = 10*1e-23 # Jansky [erg/s/cm^2/Hz]
flux = 3.63e-20 # flux of Vega [erg/s/cm^2/Hz]

# 1.

#print '1. The flux of Vega is', flux/J, '[J].'

# 2.

flux_lambda = 3.60e-9
wave = 8500.0e-8

flux_nu = conversions.convert_flux(flux_lambda, wave)
#print '2. The flux of the star is', flux_nu/J, '[J].'

# 3.

flux_star = 7.2e-14
flux_Vega = 3.6e-9

#print -2.5*math.log10(flux_star/flux_Vega)
print flux_Vega/flux_star



# freq = conversions.WaveToFreq(wave)
