import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.integrate import odeint



def dU_dx(U, x):
    
    return [U[1], -10*np.sin(2*U[0])]

U0 = [0, math.pi/4]
xs = np.linspace(0, 10, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]

plt.xlabel("x")
plt.ylabel("y")
plt.title("Pendulum")
plt.plot(xs,ys)
plt.show()
