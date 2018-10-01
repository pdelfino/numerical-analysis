import math
import numpy as np
from matplotlib import pyplot as plt
import pylab

def heun(x):
    
    y_init = 3
    x_init = 0
   
    old_dy_dx = (-1.2*y_init) + (7*(math.e**(-0.3*x_init)))
    print ("old_dy_dx: ",old_dy_dx)

    old_y = y_init 
    print ("old_y", old_y)

    new_y = None
    
    new_dy_dx = None

    delta_x = 0.5
    
    limite = 0

    while x>limite:
        
        print ("entrei no loop")
        print ("===============================")
        previous_old = old_dy_dx
        print ("previous_old", previous_old)

        new_y = delta_x*old_dy_dx + old_y
        print ("new_y ", new_y, "delta_x", delta_x,"old_dy_dx", old_dy_dx, "old_y", old_y)

        new_dy_dx = (-1.2*new_y)+(7*((math.e)**(-0.3*delta_x)))
        print ("new dy_dx: ", new_dy_dx, "new_y",new_y,"delta_x",delta_x)

        old_dy_dx = new_y
        
        k_heun = (previous_old+ new_dy_dx)/2
        print ("k de heun, média artimética", k_heun)
        
        new_y = (delta_x*k_heun) + old_y
        print ("delta_x",delta_x,"k_heun",k_heun,"old_y",old_y)

        old_y = new_y
        
        new_y = old_y

        limite = limite +delta_x
        print ("acabou a iteração, preciso ter x como ", limite,"e y como ",new_y)


    return new_y

print (heun(1.0))

"""
t = np.linspace(-1,50, 80)

lista_outputs = []

for i in t:
    lista_outputs.append(euler(i))
    print (i)

# red dashes, blue squares and green triangles
#plt.plot(t, f(t), 'b-', label='Output resultado analítico')
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Comparação Euler/Analítico - tolerância: 0.3')
pylab.legend(loc='upper left')
plt.show()"""
