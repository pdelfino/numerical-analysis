import math
import random
from numpy import array 
import numpy as np 
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline

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
#teste_dinamico = random_sine()
#x = teste_dinamico[1]
#y = teste_dinamico[3]

pares_x_y = list(zip(x,y))

sort_pares_x_y = sorted(pares_x_y)

x_ordenado = []
y_ordenado_simetric = []

for i in sort_pares_x_y:
    
    x_ordenado.append(i[0])
    y_ordenado_simetric.append(i[1])

x_ordenado = array(x_ordenado)
y_ordenado_simetric = array(y_ordenado_simetric)

# (x,y) = (0,12) (1,14) (2,22) (3,39) (4,58) (5,77)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([12,14,22,39,58,77])

x = x_ordenado
y = y_ordenado_simetric

#fixed_x = array([5.80990031, 1.7836885,  4.62073799, 0.89337425, 5.62219906])
#fixed_y = array([-0.45581264,  0.97742392, -0.99580299,  0.77919112, -0.61389568])

# calcular os VÁRIOS polinônimos da cubic spline 
cs = CubicSpline(x,y,bc_type='natural')

# para encontrar os coeficientes a0, b0, c0 e etc...
cs.c
print (cs.c)

# 0 <= x <= 1
a0 = cs.c.item(3,0)
b0 = cs.c.item(2,0)
c0 = cs.c.item(1,0)
d0 = cs.c.item(0,0)

# 1 < x <= 2
a1 = cs.c.item(3,1)
b1 = cs.c.item(2,1)
c1 = cs.c.item(1,1)
d1 = cs.c.item(0,1)

# 4 < x <= 5
a2 = cs.c.item(3,2)
b2 = cs.c.item(2,2)
c2 = cs.c.item(1,2)
d2 = cs.c.item(0,2)

# 5 < x <= 6
a3 = cs.c.item(3,3)
b3 = cs.c.item(2,3)
c3 = cs.c.item(1,3)
d3 = cs.c.item(0,3)

"""# 5 < x <= 6
a4 = cs.c.item(3,4)
b4 = cs.c.item(2,4)
c4 = cs.c.item(1,4)
d4 = cs.c.item(0,4)
"""
"""# 5 < x <= 6
a5 = cs.c.item(3,5)
b5 = cs.c.item(2,5)
c5 = cs.c.item(1,5)
d5 = cs.c.item(0,5)
"""
# Print polynomial equations for different x regions
print('S0(0<=x<=1) = ', a0, ' + ', b0, '(x-0.89) + ', c0, '(x-0.89)^2  + ', d0, '(x-0.89)^3')
print('S1(1< x<=2) = ', a1, ' + ', b1, '(x-1.78) + ', c1, '(x-1.78)^2  + ', d1, '(x-1.78)^3')
print('S2(4< x<=5) = ', a2, ' + ', b2, '(x-4.62) + ', c2, '(x-4.62)^2  + ', d2, '(x-4.62)^3')
print('S3(5< x<=6) = ', a3, ' + ', b3, '(x-5.62) + ', c3, '(x-5.62)^2  + ', d3, '(x-5.62)^3')

# Cubic spline interpolation calculus example
# https://www.youtube.com/watch?v=gT7F3TWihvk

