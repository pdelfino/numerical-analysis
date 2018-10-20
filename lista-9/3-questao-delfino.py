import mcint
import random
import numpy as np

# parametrizacao e multiplicando por jacobiano

def integrand_r(r):

    return r - (r**3)

def integrand_theta(theta):

    return 1
    
# using fubini, para separar

def sampler():
    
    while True:

        yield random.random()

############## primeira aplicacao
result_r, error = mcint.integrate(integrand_r, sampler(), measure=1.0, n=100)
print ("A integral de (r -r**3) no intervalo de 0 and 1 com Monte Carlo é, aproximadamente, ", result_r)
#print ("error",error)
#print ("\n")

############## outra aplicacao
result_theta, error = mcint.integrate(integrand_theta, sampler(), measure=2*np.pi, n=100)
print ("A integral de 1 no intervalo de 0 a 2*pi com Monte Carlo é, aproximadamente, ", result_theta)
#print ("error",error)
#print ("\n")

final_result = result_r*result_theta
print ("O resultado final da integral dupla, usando Fubini, é o produto dos anteriores, logo:  ",final_result)

print ("O resultado analítico é pi/2, portanto, um erro de aproximação de :", abs((np.pi/2)-final_result))
