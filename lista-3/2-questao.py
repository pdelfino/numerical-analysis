# implementar divided diferences
from sympy import poly as p
from sympy.abc import x

lista_exemplo = [ [0,0], [1,1], [2,2], [3,3]]

exemplo1 = [[0,-1]]
exemplo2 = [[0,-1],[1,1]]
exemplo3 = [[0,-1],[1,1],[2,5]]

def coefficient(lista):

    if len(lista)==1:

        return lista[0][1]

    else:
        length = len(lista)
        len_sub_1 = length - 1

        return (coefficient(lista[1:]) - coefficient(lista[:len_sub_1]))/(lista[len_sub_1][0]-lista[0][0])

#print (coefficient(lista_exemplo))
#print (coefficient([[0,1]]))

print (coefficient(lista_exemplo))
print (coefficient(exemplo2))

a_0 = coefficient(exemplo1)
a_1 = coefficient(exemplo2)
a_2 = coefficient(exemplo3)

print (a_0,a_1,a_2)

print (p(x*(x - 1)**2))

def divided_diferences(lista_10):

    a_0 = coefficient(lista_10[:1])
    print(lista_10[:1])
    a_1 = coefficient(lista_10[:2])
    a_2 = coefficient(lista_10[:3])
    print (lista_10[:3])
    a_3 = coefficient(lista_10[:4])
    a_4 = coefficient(lista_10[:5])
    a_5 = coefficient(lista_10[:6])
    a_6 = coefficient(lista_10[:7])
    a_7 = coefficient(lista_10[:8])
    a_8 = coefficient(lista_10[:9])
    a_9 = coefficient(lista_10[:10])

    print (a_9,a_8,a_7,a_6,a_5,a_4,a_1,a_2,a_3)

lista_fodase = []

for i in range(1,11):
    lista_fodase.append([i+4,i+1])

#print (lista_fodase)

print (divided_diferences(lista_fodase))
