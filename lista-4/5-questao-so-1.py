import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = np.array([-31, -28, -17, 0,  0,  0 ,  6,  39, 63])
y = np.array([  0, -28,  17, 0, 16, -47,  6, -39,  0])

arr = np.arange(np.amin(x), np.amax(x), 0.01)
s = interpolate.CubicSpline(x, y)
plt.plot(x, y, 'bo', label='Data Point')
plt.plot(arr, s(arr), 'r-', label='Cubic Spline')
plt.legend()
plt.show()

