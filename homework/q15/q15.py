'''
Input four combinations of total source photons and total
background photons and calculate the signal-to-noise,
instrumental magnitude, and the magnitude uncertainty.
'''

import math
import numpy as np

S1 = 10.
S2 = 100.
B1 = 0.
B2 = 100.

SN1 = S1/math.sqrt(S1+B1)
SN2 = S1/math.sqrt(S1+B2)
SN3 = S2/math.sqrt(S2+B1)
SN4 = S2/math.sqrt(S2+B2)

m1 = -2.5*math.log10(S1)
m2 = -2.5*math.log10(S1)
m3 = -2.5*math.log10(S2)
m4 = -2.5*math.log10(S2)

sigma_m1 = 1.788/S1
sigma_m2 = 1.788/S1
sigma_m3 = 1.788/S2
sigma_m4 = 1.788/S2

print SN1, SN2, SN3, SN4
print m1, m2, m3, m4
print sigma_m1,sigma_m2,sigma_m3,sigma_m4,
