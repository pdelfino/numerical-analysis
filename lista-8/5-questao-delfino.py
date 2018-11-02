import numpy as np
import matplotlib.pyplot as plt

#sortear 100 pontos igualmente espaçados
pontos_x_coor = np.linspace(0,1,100)

print ("O resultado analítico é ",np.pi, " (pi)")
analitic_pi = np.pi

def f(x):

    return 4/(1+(x**2))

def trapezoidal_rule(start,end):

    return (end-start)*(f(start)+f(end))/2

def all_trapezoidal(points):
    
    total = 0

    for i in range(0,len(points)-1):

        total = total + trapezoidal_rule(points[i],points[i+1])

    return total

def romberg(f):
    
    Matrix = np.zeros((5,5),float)
    
    for i in range(0,5):
        
        Matrix[i,0] = all_trapezoidal(pontos_x_coor)
        
        for k in range(0,i):
            
            n = k + 2
            
            Matrix[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Matrix[i,k] - Matrix[i-1,k])
    
    return (Matrix[i,k+1])

ro = romberg(f)

print ("Diferença entre o resultado analítico e a aproximação via método de Romberg de ordem 5 é: ", abs(ro - np.pi))


