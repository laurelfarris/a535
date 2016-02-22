import math


k = -0.4
z = 22.3
z = math.radians(z)
s = 1./(math.cos(z))

X = s-0.0018167*(s-1)-0.002875*(s-1)**2-0.0008083*(s-1)**3

delta_mag = k*X
print delta_mag

print 360./24
