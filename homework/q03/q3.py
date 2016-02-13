import math

# distance to Earth (E) and Jupiter (J) [cm]
d_E = 1.5e13
d_J = 7.5e13

# radius [cm], mass [g], and luminiosity [erg s^-1] of the sun
R_sun = 6.96e10
M_sun = 2.0e33
L_sun = 3.9e33

F_E = L_sun/(4.0*(math.pi)*(d_E**2))
F_J = L_sun/(4.0*math.pi*d_J**2)

# solar 'constants'
print 'solar constants:'
print 'earth: {:.2e} [erg s^-1 cm^-2]'.format(F_E)
print 'jupiter: {:.2e} [erg s^-1 cm^-2]'.format(F_J)

theta_E = (math.pi*R_sun**2)/(d_E**2)
theta_J = (math.pi*R_sun**2)/(d_J**2)

print 'surface brightness'
print 'earth: {:.2e}'.format(F_E/theta_E)
print 'jupiter: {:.2e}'.format(F_J/theta_J)
