import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

global h

h = 0.1

def euler_second_order(x_input):

    z_init = 0
    x_init = 0
    y_init = (math.pi)/4

    x_old = x_init
    y_old = y_init
    z_old = z_init

    limite = 0

    while x_input>limite:
    
        #print ("nova iteracao")
        #print ("===================")

        y_iter = y_old + (h*z_old)
        z_iter = z_old + (h*(-10*(math.sin(y_old))))

        x_old = h + x_old

        y_old = y_iter

        z_old = z_iter

        limite = limite + h

    return y_iter, z_iter

t = np.linspace(1,100,100)

y_x_vals = []

for i in t:
    y_x_vals.append(euler_second_order(i)[0])

dy_dx = []

for i in t:
    dy_dx.append(euler_second_order(i)[1])

#plt.plot(t, g(t), 'b-', label='Output resultado analítico')
plt.plot(dy_dx, y_x_vals, 'ro', label="Output resultado numérico Euler para equação de segunda Ordem")
plt.title('Comparação Euler/Analítico - tolerância: ' + str(h))
pylab.legend(loc='upper left')
plt.xlabel('Derivada de Theta em relação a t')
plt.ylabel('Theta')

"""plt.plot(t , y_x_vals, 'ro', label="Output resultado numérico Euler para equação de segunda Ordem")
plt.title('Comparação Euler/Analítico - tolerância: ' + str(h))
pylab.legend(loc='upper left')"""

plt.show()

