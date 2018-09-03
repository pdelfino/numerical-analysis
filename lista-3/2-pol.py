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

print (lista_fixa_testes)


