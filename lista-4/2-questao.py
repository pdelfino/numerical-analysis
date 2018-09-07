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

"""
caso deseje usar os valores fixos
basta inserir o comentário "#" nas linhas
39, 40 e 41 abaixo
"""
teste_dinamico = random_sine()
x = teste_dinamico[1]
y = teste_dinamico[3]

time = np.arange(0,10,0.1)

amplitude = np.sin(time)

plot.plot(time, amplitude)

plot.title('Função Seno')

plot.xlabel('Coordenadas de X')

plot.ylabel('Seno(x)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

pares_x_y = list(zip(x,y))

sort_pares_x_y = sorted(pares_x_y)

x_ordenado = []
y_ordenado_simetric = []

for i in sort_pares_x_y:
    
    x_ordenado.append(i[0])
    y_ordenado_simetric.append(i[1])

x_ordenado = array(x_ordenado)
y_ordenado_simetric = array(y_ordenado_simetric)

f = interp1d(x_ordenado, y_ordenado_simetric)

f2 = interp1d(x_ordenado, y_ordenado_simetric, kind="cubic")

plot.plot(x_ordenado, f2(x_ordenado))

minimo = min(x_ordenado)
maximo = max(x_ordenado)

xnew = np.linspace(minimo, maximo, num=400, endpoint=True)

plot.plot(x_ordenado, y_ordenado_simetric, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')

plot.scatter(x,y)

plot.show()

