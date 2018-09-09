import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = np.array([-31, -28,  0, 39, 63])
y = np.array([  0, -28, -47, -39, 0])

arr = np.arange(np.amin(x), np.amax(x), 0.01)
s = interpolate.CubicSpline(x, y)
plt.plot(x, y, 'bo', label='Data Point')
plt.plot(arr, s(arr), 'r-', label='Cubic Spline')

k = np.array([ -31, -17,  0, 6])
l = np.array([   0,  17, 16, 6])

akk = np.arange(np.amin(k), np.amax(k), 0.01)
t = interpolate.CubicSpline(k,l)
plt.plot(k, l, 'bo', label='Data Point')
plt.plot(akk, t(akk), 'r-', label='Cubic Spline')

plt.legend()
plt.show()

