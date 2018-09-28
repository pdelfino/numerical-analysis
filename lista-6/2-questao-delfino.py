import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

interval = [0,5]

def f(x):

    return (math.e)**(-10*x)

def y_t_plus_h(h,y):

    return y/(1+10*h)

def implicit_euler(y_t_plus_h,h, interval):
    
    x_init = 0
    y_init = 1
    
    old_y = y_init
    old_t = x_init
    
    new_t = []
    new_t.append(old_t)

    new_y = []
    new_y.append(old_y)
    
    while old_t < interval[1]:
        
        y = y_t_plus_h(h, old_y)
        
        new_y.append(y)
        new_t.append(old_t+h) 
        
        old_y = y
        old_t = old_t + h
    
    return new_t, new_y

h = 0.2
t = (implicit_euler(y_t_plus_h,h,interval))[0]
lista_outputs = (implicit_euler(y_t_plus_h,h,interval))[1]

output_analitico = []

for i in t:
    output_analitico.append(f(i))

plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.plot(t, output_analitico, 'b-', label='Output resultado analítico')
plt.title('Comparação Euler/Analítico - tolerância: '+ str(h))
pylab.legend(loc='upper left')
plt.show()
