import math

def f_example(x):

    return x**2

def gaussian_quadrature_3(f):
    
    coef_1 = 5/9

    coef_2 = 8/9

    x_input = math.sqrt(0.6)

    return (coef_1*f(-x_input)) + (coef_2*f(0)) + (coef_1*f(x_input))

print (gaussian_quadrature_3(f_example))



