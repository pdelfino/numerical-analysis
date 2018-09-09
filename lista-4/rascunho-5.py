import math
import random
from numpy import array 
import numpy as np 
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d

x = array([0, 6, 0, -17, -31, -28, 0, 39, 63])
y = array([0, 6, 16, 17, 0, -28, -47, -39, 0])

time = np.arange(0,10,0.1)

plot.title('Espiral')

plot.xlabel('X')

plot.ylabel('Y')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

f = interp1d(x, y)

f2 = interp1d(x, y, kind="cubic")

plot.plot(x, f2(x))

minimo = min(x)
maximo = max(x)

xnew = np.linspace(minimo, maximo, num=400, endpoint=True)

plot.plot(x, y, 'o',  xnew, f2(xnew), '--')

plot.scatter(x,y)

plot.show()

