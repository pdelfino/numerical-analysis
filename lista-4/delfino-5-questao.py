import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plot

x = np.array([0, 6,   0, -17, -31, -28,   0,  39, 63])
y = np.array([0, 6,  16,  17,   0, -28, -47, -39,  0])

x = np.r_[x, x[0]]
y = np.r_[y, y[0]]

tck = (interpolate.splprep([x, y], s=0, per=True))[0]
u = (interpolate.splprep([x, y], s=0, per=True))[1]

xi = (interpolate.splev(np.linspace(0, 1, 1000), tck))[0]
yi = (interpolate.splev(np.linspace(0, 1, 1000), tck))[1]

fig, ax = plot.subplots(1, 1)
ax.plot(x, y, 'or')
ax.plot(xi, yi, '-b')

plot.show()
