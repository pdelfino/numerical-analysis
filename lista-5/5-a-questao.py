#fazer série de Taylor https://www.youtube.com/watch?v=aZB8ffWQI1k
#optei por não usar o pacote simbólico
import math
import numpy as np
import matplotlib.pyplot as plt
import pylab 

def questao_1_a(x):

    return 1 + x + ((x**2)/2)

def f(x):

    return (math.e)**x

"""def questao_1_b(x):

    return (x**2)/2

def g(x):

    return math.sqrt((x**2)+1) - 1
"""

t = np.linspace(0,1, 10)

lista_outputs = []

for i in t:
    lista_outputs.append(questao_1_a(i))

# red dashes, blue squares and green triangles
plt.plot(t, f(t), 'bs', label='Output resultado analítico')
plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
plt.title('Comparação Euler/Analítico - tolerância: 0.1')
pylab.legend(loc='upper left')
plt.show()

