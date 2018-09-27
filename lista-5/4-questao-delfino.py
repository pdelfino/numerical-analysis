#fazer série de Taylor https://www.youtube.com/watch?v=aZB8ffWQI1k
#optei por não usar o pacote simbólico

import math

def questao_1_a(x):

    return 1 + x + ((x**2)/2)

#print (questao_1_a(0.5))

def f(x):

    return (math.e)**x

print ("função analítica f(x)=e^x com input x=0.25: ", f(0.25))
print ("função de aproximação numérica usando Taylor de ordem 2 com input x=0.25: ", questao_1_a(0.25))
print ("conclusão: a aproximação é muito boa")

def questao_1_b(x):

    return (x**2)/2

def g(x):

    return math.sqrt((x**2)+1) - 1

print ("\n")
print ("função analítica do enunciado 1-b com input x=0.825: ", g(0.125))
print ("função de aproximação numérica usando Taylor de ordem 2 com input x=0.825: ", questao_1_b(0.125))
print ("conclusão: a aproximação é razoável")


