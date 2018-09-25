import math
import numpy as np
import matplotlib.pyplot as plt
import pylab 

def analitic(x):

    return (np.sqrt(1+(x**2))) - 1

"""
print (analitic(0.1))
print (analitic(0.5))
print (analitic(0.8))
"""

def euler(x):
   
    y_init = 0

    x_init = 0
    
    old_dy_dx = x_init/(1+y_init)

    old_y = y_init 

    new_y = None
    
    new_dy_dx = None
    
    h  = 0.1
    
    limite = 0
    
    i = 0
    
    x_new = x_init

    while x>=limite:
        
        i+=1
        #print ("iterada", i)

        new_y = (h*old_dy_dx) + old_y
        #print ("new_y", new_y)
        
        x_new += h
        
        new_dy_dx =  x_new/(1+new_y)
        #print ("new dy_dx", new_dy_dx)

        old_y = new_y

        old_dy_dx = new_dy_dx
        
        limite = limite + h

    return new_y

print (euler(0.8),analitic(0.8))

t = np.linspace(0,1,5)

lista_outputs = []

for i in t:
    lista_outputs.append(euler(i))

print (lista_outputs)
plt.plot(t, analitic(t), 'bs', label='Output resultado analítico')
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Comparação Euler/Analítico - tolerância: 0.1')
pylab.legend(loc='upper left')
plt.show()
