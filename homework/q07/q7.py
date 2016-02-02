import math
import pdb

# Import 'conversions.py' from question 5
import conversions

# 1.
J = 10*1e-23 # Jansky [erg/s/cm^2/Hz]
wave = 5500.0e-8 # Wavelength [cm]
flux_lambda = 3.6e-9 # flux of Vega [erg/s/cm^2/Angstrom]
flux_nu = conversions.convert_flux(flux_lambda,wave)
            # flux of Vega [erg/s/cm^2/Hz]
print flux_nu
print '1. The flux of Vega is', flux_nu/J, '[J].'

# 2.

flux_lambda = 3.60e-9 # flux of star [erg/s/cm^2/Angstrom]
wave = 8500.0e-8 # wavelength of star [cm]
flux_nu = conversions.convert_flux(flux_lambda,wave)
            # flux of star [erg/s/cm^2/Hz]
print '2. The flux of the star is', flux_nu/J, '[J].'

# 3.

flux_star = 7.2e-14 # flux of star [erg/s/cm^2/Angstrom]
flux_Vega = 3.6e-9 # flux of Vega [erg/s/cm^2/Angstrom]

print '3. The difference in magnitudes is'
print -2.5*math.log10(flux_star/flux_Vega)
print 'and the star is', flux_Vega/flux_star
print 'times fainter than Vega.'



# freq = conversions.WaveToFreq(wave)
