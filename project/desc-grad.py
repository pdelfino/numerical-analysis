
import numpy as np

print ("De acordo com Wikipedia, melhor step-size possível")
print ("\n")

def grad(x1,grad,max_iter):
    x0 = x1 - 0.001
    i = 0
    while (abs(x1 - x0) > 0.00001) and (max_iter > i):
        gamma = (x1-x0)*(grad(x1)-grad(x0))/((grad(x1)-grad(x0))**2)
        x0 = x1
        x1 = x1 - gamma*grad(x0)
        i += 1
        print("iterativo: ", x0)
    print("Resultado iterativo final: ", x1)

def f1(x):
    return(4*x**3 - 9*x**2)

grad(6,f1,10000)

print ("\n")
print ("Repetindo a implementação com outro step-size")
print ("\n")

def grad2(x1,grad,max_iter):
    x0 = x1 - 0.01
    i = 0
    while (abs(x1 - x0) > 0.00001) and (max_iter > i):
        gamma = 0.019
        x0 = x1
        x1 = x1 - gamma*grad(x0)
        i += 1
        print("iterativo: ", x0)
    print("Resultado iterativo final: ",x1)

grad2(6,f1,1000)

############

#f(x) = x^4-4x^3-2x^2 + 5x + 9
def f2(x):
    return(4*x**3 - 12*x**2 - 4*x + 5)

grad(-1,f2,100000)

grad(4,f2,100000)
