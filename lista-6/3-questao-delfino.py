import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

def g(x):

    return (math.e)**(x)

#(-1.2*y_init) + (7*(math.e**(-0.3*x_init)))

global h 
h = 0.1

def heun(x):
    
    y_init = 1
    
    x_init = 0
    
    limite = 0
    
    y_old = y_init

    y_new = None

    x_old = x_init

    x_new = None 

    while x>limite:
        
        #print ("entrei no loop")
        #print ("========================")
        #print ("h",h, "x_old",x_old,"y_old",y_old)

        k1 = y_old
        #print ("k1,",k1)

        x_new = x_old + h
        #print ("x_new", x_new)

        y_new = y_old + k1*h
        #print ("y_new", y_new)

        k2 = y_new
        #print ("k2", k2)

        kh = (k1+k2)/2
        #print ("kh da divisão", kh)

        y_new = y_old + (kh*h)
        #print ("y_new", y_new)

        #print ("x_new", x_new)

        y_old = y_new
        x_old = x_new

        limite = limite + h
        #print ("acabou a iteração, preciso ter x como ", ,"e y como ",new_y)

    return y_new

#print (heun(1.5),g(1.5))

t = np.linspace(-1,3, 18)

lista_outputs = []

for i in t:
    lista_outputs.append(heun(i))
    #print (i)

plt.plot(t, g(t), 'b-', label='Output resultado analítico')
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Comparação Euler/Analítico - tolerância: ' + str(h))
pylab.legend(loc='upper left')
plt.show()
