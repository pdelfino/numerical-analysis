from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 70)
y = np.sin(x)

spl = UnivariateSpline(x,y,k=3)

print (x)
print (spl)

#spl.derivative()

plt.plot(x, spl)

