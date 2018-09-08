import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

x1 = [1., 0.88,  0.67,  0.50,  0.35,  0.27, 0.18,  0.11,  0.08,  0.04,  0.04,  0.02]
y1 = [0., 13.99, 27.99, 41.98, 55.98, 69.97, 83.97, 97.97, 111.96, 125.96, 139.95, 153.95]

#x = array([0, 6, 0, -17, -31, -28, 0, 39, 63])
#y = array([0, 6, 16, 17, 0, -28, -47, -39, 0])

# Combine lists into list of tuples
points = zip(x1, y1)

# Sort list of tuples by x-value
points = sorted(points, key=lambda point: point[0])

# Split list of tuples into two list of x values any y values
x1, y1 = zip(*points)

new_length = 25
new_x = np.linspace(min(x1), max(x1), new_length)
new_y = sp.interpolate.interp1d(x1, y1, kind='slinear')(new_x)
