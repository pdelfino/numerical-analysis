import math
import numpy as np
import matplotlib.pyplot as plt
import pylab 

def euler(x):
   
    y_init = 0

    x_init = 0
    
    old_dy_dx = x/(x+y_init)

    old_y = y_init 

    new_y = None
    
    new_dy_dx = None

    delta_x = 0.00001
    
    limite = 0

    while x>=limite:

        #for i in range(1,6):
        
        new_y = delta_x*old_dy_dx + old_y
        #print ("new_y", new_y)

        new_dy_dx =  delta_x/(delta_x+new_y)
        #print ("new dy_dx", new_dy_dx)

        old_y = new_y
        #print ("old_y", old_y)

        old_dy_dx = new_y
        #print ("old delta y_delta x", old_dy_dx, "iterada", i)
        
        limite = limite +delta_x

        delta_x += 0.1

    return new_y

#print (euler(0.1))

t = np.random.uniform(0,10,100)

lista_outputs = []

for i in t:
    lista_outputs.append(euler(i))

#print (lista_outputs)
# red dashes, blue squares and green triangles
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Método de Euler versus Analítico  tolerância: 0.1')
pylab.legend(loc='upper left')
plt.show()

