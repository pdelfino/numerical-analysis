import math
import random
from numpy import array 
import numpy as np 
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d

def random_sine():
    
    lista_f_x = []
    lista_x = []
    
    for i in range(1,6):
        
        aleatorio = random.uniform(0,360)
        aleatorio = math.radians(aleatorio)
        lista_x.append(aleatorio)

        sin_rand = math.sin(aleatorio)
        lista_f_x.append(sin_rand)

    lista_x = array(lista_x)
    lista_f_x = array(lista_f_x)

    return ("x",lista_x,"f(x)", lista_f_x) 

print (random_sine()[1])

fixed_x = array([5.80990031, 1.7836885,  4.62073799, 0.89337425, 5.62219906])
fixed_y = array([-0.45581264,  0.97742392, -0.99580299,  0.77919112, -0.61389568])

x = fixed_x
y = fixed_y

teste_dinamico = random_sine()
print (teste_dinamico,teste_dinamico[1],teste_dinamico[3])

#x = teste_dinamico[1]
#y = teste_dinamico[3]
time = np.arange(0,10,0.1)

amplitude = np.sin(time)

plot.plot(time,amplitude)

plot.plot(time, amplitude)

plot.title('Função Seno')

plot.xlabel('Coordenadas de X')

# Give y axis label for the sine wave plot

plot.ylabel('Seno(x)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

x_ordenado = array([0.89337425, 1.7836885, 4.62073799, 5.62219906, 5.80990031])

y_ord_ac_x = array([0.77919112, 0.97742392, -0.99580299, -0.61389568 , -0.45581264,])

f = interp1d(x_ordenado, y_ord_ac_x)
f2 = interp1d(x_ordenado, y_ord_ac_x, kind="cubic")
print (f2)
plot.plot(x_ordenado, f2(x_ordenado))
xnew = np.linspace(1, 4, num=41, endpoint=True)

plot.plot(x_ordenado, y_ord_ac_x, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')

plot.scatter(x,y)

plot.show()

