import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

global h

h = 0.001

def euler_second_order(x_input):

    z_init = 13
    x_init = 0
    y_init = 7

    x_old = x_init
    y_old = y_init
    z_old = z_init

    #f_1 = ((11*(math.e**(-1*x_old)))-(3*z_old)-(5*y_old))/2
    #f_2 = z_old

    limite = 0

    while x_input>limite:
    
        #print ("nova iteracao")
        #print ("===================")

        y_iter = y_old + (h*z_old)
        #print ("y_iter", y_iter, "y_old", y_old, "h",h,"x_old",x_old,"y_old",y_old,"z_old",z_old)
        z_iter = z_old + (h*(((11*(math.e**(-x_old)))-(3*z_old)-(5*y_old))/2))

        x_old = h + x_old

        y_old = y_iter

        z_old = z_iter

        limite = limite + h

    return y_iter, z_iter

print (euler_second_order(4.50))

t = np.linspace(1,30, 300)

y_x_vals = []

for i in t:
    y_x_vals.append(euler_second_order(i)[0])

dy_dx = []

for i in t:
    dy_dx.append(euler_second_order(i)[1])

"""#plt.plot(t, g(t), 'b-', label='Output resultado analítico')
plt.plot(dy_dx, y_x_vals, 'ro', label="Output resultado numérico Euler para equação de segunda Ordem")
plt.title('Comparação Euler/Analítico - tolerância: ' + str(h))
pylab.legend(loc='upper left')"""

plt.plot(t , y_x_vals, 'ro', label="Output resultado numérico Euler para equação de segunda Ordem")
plt.title('Comparação Euler/Analítico - tolerância: ' + str(h))
pylab.legend(loc='upper left')

plt.show()

