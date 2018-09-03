import math
import numpy

#print (numpy.random.uniform())
def exercise_function(x):

    return (math.cos(math.pi*x))

def random_points():
    
    lista_pontos = []

    for i in range(1,11):

        lista_pontos.append(numpy.random.uniform(-1,1))

    return lista_pontos

lista_fixa_testes = [0.19749031528693695, -0.35269067224638695, -0.46945499921828526,
                     0.9347420379124274, 0.17623436492386224, 0.5071727904865755,
                     - 0.8848487037050465, -0.0007892065095642664, -0.2860599703093776,
                     - 0.7096061858165912]

#print (lista_fixa_testes)

#######################################
ponto_1 = [0,-1]

ponto_2 = [1,1]

ponto_3 = [2,5]


lista_tuplas = [(0,-1),(1,1),(2,5)]

example_primeira_parte = [(0,-1),(1,1)]
example_segunda_parte = [(1,1),(2,5)]

def diff_duas_tuplas(lista_2_tuplas):

    nume = lista_2_tuplas[0][1] - lista_2_tuplas[1][1]
    deno = lista_2_tuplas[0][0] - lista_2_tuplas[1][0]
    
    return (nume/deno)

print (diff_duas_tuplas(example_primeira_parte))
print (diff_duas_tuplas(example_segunda_parte))


def diff_3(lista_3_tuplas):

    deno = lista_3_tuplas[0][0] - lista_3_tuplas[len(lista_3_tuplas)-1][0]

    nume = diff_duas_tuplas(lista_3_tuplas[0:2]) - diff_duas_tuplas(lista_3_tuplas[1:3])

    return nume/deno

print (diff_3(lista_tuplas))


def newton_3_points(lista_tuplas):
    
    initial_y = lista_tuplas[0][1]

    first = lista_tuplas[0][0]

    second = lista_tuplas[1][0]
    
    #out = initial_y + (x -first)*diff_duas_tuplas(lista_tuplas[0:2] #+ (x - first)*(x - second)*(diff_3_tuplas(lista_tuplas) 

    return out

print (newton_3_points(lista_tuplas))
