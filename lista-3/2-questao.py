from sympy import poly as p
from sympy.abc import x
import numpy as np
import matplotlib.pylab as plot

lista_exemplo = [[0,0],[1,1], [2,2], [3,3]]
exemplo1 = [[0,-1]]
exemplo2 = [[0,-1],[1,1]]
exemplo3 = [[0,-1],[1,1],[2,5]]
exemplo_livro = [[1,3],[3/2,13/4],[0,3],[2,5/3]]

def coefficient(lista):

    if len(lista)==1:

        return lista[0][1]

    else:
        length = len(lista)
        len_sub_1 = length - 1

        return (coefficient(lista[1:]) - coefficient(lista[:len_sub_1]))/(lista[len_sub_1][0]-lista[0][0])

def lista_coeficientes(l_p):
   
    lista_coef = []
    
    for i in range(1,len(l_p)+1):
        
        elemento = (coefficient(l_p[:i]))
        lista_coef.append(elemento)

    return lista_coef

#print (lista_coeficientes(exemplo_livro))

def caso_dois(x, l_p):
    
    c_f = lista_coeficientes(l_p)
    
    total=  (c_f[0]
            + c_f[1]*(x-l_p[0][0])
            + c_f[2]*(x-l_p[0][0])*(x-l_p[1][0]))

    return total


def caso_tres(x, l_p):
    
    c_f = lista_coeficientes(l_p)
    
    total=  (c_f[0]
            + c_f[1]*(x-l_p[0][0])
            + c_f[2]*(x-l_p[0][0])*(x-l_p[1][0])
            + c_f[3]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0]))

    return total

#print (caso_tres(2, exemplo_livro))
print (caso_dois(0, exemplo3))

def sample_cosine():
    
    x_vals = np.linspace(-1,1,10)

    lista = []

    for val in x_vals:

        lista.append([val,np.cos(np.pi*val)])

    return lista

#print (sample_cosine())
pontos_cosseno = sample_cosine()
#print (lista_coeficientes(pontos_cosseno))

def interpolate_10(x, l_p):
   
    # c_f means coeficient list
    c_f = lista_coeficientes(l_p)
    
    init = c_f[0]
    one = c_f[1]*(x-l_p[0][0])
    two = c_f[2]*(x-l_p[0][0])*(x-l_p[1][0])
    third = c_f[3]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])
    fourth = c_f[4]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])
    fifth = c_f[5]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])*(x-l_p[4][0])
    sixth = c_f[6]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])*(x-l_p[4][0])*(x-l_p[5][0])
    sventh = (c_f[7]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])*(x-l_p[4][0])*(x-l_p[5][0])*(x-l_p[6][0]))
    eigth = ((c_f[8]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])*(x-l_p[4][0])*(x-l_p[5][0])*(x-l_p[6][0]))*(x-l_p[7][0]))
    nine = ((c_f[8]*(x-l_p[0][0])*(x-l_p[1][0])*(x-l_p[2][0])*(x-l_p[3][0])*(x-l_p[4][0])*(x-l_p[5][0])*(x-l_p[6][0]))*(x-l_p[7][0])**(x-l_p[8][0]))
 


    total = init+one+two+third+fourth+fifth+sixth+sventh+eigth+nine

    return total
#gerar pontos da função cos pix
x = np.linspace(-1,1,10)
#print (x)

#print (interpolate_10(1/2, pontos_cosseno))

#plot.plot(x,np.cos(np.pi*x))

#print (interpolate_10(0.5,pontos_cosseno))
#plot.plot(x,interpolate_10(x,pontos_cosseno))

#plot.show()


