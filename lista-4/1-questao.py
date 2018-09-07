import math
import random

def random_sine():
    
    lista_pontos = []

    for i in range(1,6):

        aleatorio = random.uniform(0,360)
        aleatorio = math.radians(aleatorio)
        sin_rand = math.sin(aleatorio)
        #print (sin_rand, aleatorio)
        lista_pontos.append(sin_rand)

    return lista_pontos

#print (random_sine())
#print (math.sin(math.radians(45)))

#fixed_list = [-0.45742958217189966, -0.2372176562484392, -0.9784096060698162, 0.968721456456446, -0.8904037209821772]

#print (fixed_list)

print ("lista com 5 valores aleatórios da função seno de x no intervalo 0 a 2pi", random_sine())
