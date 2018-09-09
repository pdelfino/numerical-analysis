import math
import random
from numpy import * 
import matplotlib.pyplot as plt

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

#print (random_sine())
#print (math.sin(math.radians(45)))

print ("lista com as coordenadas x no intervalo [0,2pi] e as coordenadas de y após input de x na função seno:")
print (random_sine())

