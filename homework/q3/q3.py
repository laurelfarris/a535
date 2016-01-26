import math

d_E = 1.5e13
d_J = 7.5e13

R_sun = 6.96e10
M_sun = 2.0e33
L_sun = 3.9e33

F_E = L_sun/(4.0*math.pi*d_E**2)
F_J = L_sun/(4.0*math.pi*d_J**2)
theta_E = (2.0*math.atan(R_sun/d_E))**2
theta_J = (2.0*math.atan(R_sun/d_J))**2

print 'earth: ', F_E/theta_E
print 'jupiter: ', F_J/theta_J
