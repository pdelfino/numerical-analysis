import math


def gaussian_quadrature_3(f):
    
    coef_1 = 5/9

    coef_2 = 8/9

    x_input = math.sqrt(0.6)

    return (coef_1*f(-x_input)) + (coef_2*f(0)) + (coef_1*f(x_input))

def f_example_1(x):

    return x**2

print ("O resultado analítico da integral de (x^2) em [-1,1] é 0.667, a aproximação numérica: ",gaussian_quadrature_3(f_example_1))

def f_example_2(x):

    return 0

print ("O resultado analítico da integral de (0) em [-1,1] é 0, a aproximação numérica: ",gaussian_quadrature_3(f_example_2))

def f_example_3(x):

    return (2*(x**3))+(3*(x**2))+(x**1)+(9*(x**0)) 

print ("O resultado analítico da integral de (2*x^3 + 3*x^2 + x + 9) em [-1,1] é 20, a aproximação numérica: ",gaussian_quadrature_3(f_example_3))

def f_example_4(x):

    return (20*(x**4)) 

print ("O resultado analítico da integral de (20*x^4) em [-1,1] é 8, a aproximação numérica: ",gaussian_quadrature_3(f_example_4))

def f_example_5(x):

    return (x**6) 

print ("O resultado analítico da integral de (x^6) em [-1,1] é 0.28571, a aproximação numérica: ",gaussian_quadrature_3(f_example_5))

print("Percebe-se que a quadratura gaussiana funciona bem até polinômis de grau 5")


