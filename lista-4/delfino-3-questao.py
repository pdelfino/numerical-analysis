from scipy import interpolate
import math
import random
from numpy import array 
import numpy as np 
import matplotlib.pyplot as plot

def random_sine():
    
    lista_f_x = []
    lista_x = []
    
    for i in range(1,6):
        
        aleatorio = random.uniform(0,360)
        aleatorio = math.radians(aleatorio)
        lista_x.append(aleatorio)

        sine_random = math.sin(aleatorio)
        lista_f_x.append(sine_random)

    lista_x = array(lista_x)
    lista_f_x = array(lista_f_x)

    return ("x",lista_x,"f(x)", lista_f_x) 

# para ter um grupo controle melhor, deixe esses valores aleatórios, gerados uma vez, como fixos
fixed_x = array([5.80990031, 1.7836885,  4.62073799, 0.89337425, 5.62219906])
fixed_y = array([-0.45581264,  0.97742392, -0.99580299,  0.77919112, -0.61389568])

x = fixed_x
y = fixed_y

pares_x_y = list(zip(x,y))

sort_pares_x_y = sorted(pares_x_y)

x_ordenado = []
y_ordenado_simetric = []

for i in sort_pares_x_y:
    
    x_ordenado.append(i[0])
    y_ordenado_simetric.append(i[1])

x_ordenado = array(x_ordenado)
y_ordenado_simetric = array(y_ordenado_simetric)


x = np.linspace(0,360,250)
#print (x)
x_radians = [math.radians(element) for element in x]
#print (x_radians)

def f_spline(x,y,inp):

    tck = interpolate.splrep(x, y,k=3)
    
    return interpolate.splev(inp, tck)

#print (f_spline(x_ordenado,y_ordenado_simetric,0.89337425))
#print (math.sin(0.89337425))
squared_error = 0

for elemento in x_radians:

   # print ("elemento",elemento,"seno dele",math.sin(elemento),"spline do elemento", f_spline(x_ordenado, y_ordenado_simetric,elemento))
   squared_error += (math.sin(elemento)-f_spline(x_ordenado,y_ordenado_simetric,elemento))**2

mean_squared_erro = squared_error/len(x_radians)

print ("erro quadrado médio:", mean_squared_erro)
