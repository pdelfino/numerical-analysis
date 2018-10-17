import numpy as np

#sortear 100 pontos igualmente espaçados
pontos_x_coor = np.linspace(0,1,100)

print ("O resultado analítico é ",np.pi, " (pi)")
analitic_pi = np.pi

def f(x):

    return 4/(1+(x**2))

#print (f(0.5))
#print (f(0.3))

def trapezoidal_rule(start,end):

    return (end-start)*(f(start)+f(end))/2

#print (trapezoidal_rule(pontos_x_coor[0],pontos_x_coor[1]))

def all_trapezoidal(points):
    
    total = 0

    for i in range(0,len(points)-1):

        total = total + trapezoidal_rule(points[i],points[i+1])

    return total

resultado_trapezio = all_trapezoidal(pontos_x_coor)
print ("Integração via Regra do Trapézio ", resultado_trapezio)

diff_trape_analitic = resultado_trapezio - analitic_pi
diff_trape_analitic = abs(diff_trape_analitic)

print ("Diferença entre o resultado analítico e a aproximação via regra do Trapézio ", diff_trape_analitic)

def simpson(start,end):

    avg = (start + end)/2

    return ((f(start)+f(end)+(4*f(avg)))*(end-start))/6

def all_simpson(points):

    total = 0

    for i in range(0,len(points)-1):

        total = total +simpson(points[i],points[i+1])

    return total

resultado_simpson = (all_simpson(pontos_x_coor))
print ("Integração via Regra de Simpson ", resultado_simpson)

diff_simpson_analitic = resultado_simpson - analitic_pi
diff_simpson_analitic = abs(diff_simpson_analitic)
print ("Diferença entre o resultado analítico e a aproximação via regra de Simpson ", diff_simpson_analitic)

