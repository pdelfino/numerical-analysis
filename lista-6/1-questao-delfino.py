import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

def f(x):

    return (math.e)**(-10*x)


def euler(x):
    
    y_init = 1
    x_init = 0
    
    old_dy_dx = -10*y_init

    old_y = y_init 

    new_y = None
    
    new_dy_dx = None

    delta_x = 0.3
    
    limite = 0

    while x>limite:

        #for i in range(1,6):
        
        new_y = delta_x*old_dy_dx + old_y
        #print ("new_y", new_y)

        new_dy_dx = -10*new_y
        #print ("new dy_dx", new_dy_dx)

        old_y = new_y
        #print ("old_y", old_y)

        old_dy_dx = new_y
        #print ("old delta y_delta x", old_dy_dx)
        #print ("iterada",i)
        
        limite = limite +delta_x

    return new_y

t = np.linspace(-1,50, 80)

lista_outputs = []

for i in t:
    lista_outputs.append(euler(i))
    print (i)


# red dashes, blue squares and green triangles
plt.plot(t, f(t), 'b-', label='Output resultado analítico')
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Comparação Euler/Analítico - tolerância: 0.3')
pylab.legend(loc='upper left')
plt.show()
