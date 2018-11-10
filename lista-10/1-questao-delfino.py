import math

n = 10

m = 20

h = 0.1

k = 0.005

u_0 = 0

v_0 = 0

u_n = 0

v_n = 0

lista_u_i = []

for i in range(0, n):

    lista_u_i.append(math.sin(math.pi*i*h))

#print (len(lista_u_i))

lista_v_i = []

nova_u_i = []

for j in range(0, m):

    for i in range(0,n-1):
        
        val = (lista_u_i[i]+lista_u_i[i+1])/2

        lista_v_i.append(val)

    t=j*k

    for i_two in range(0,n-1):
        
        val = (math.e)**((-1)*((math.pi)**2)*t)
        val = (val*math.sin(math.pi*i*h)) - (lista_v_i[i_two])
        nova_u_i.append(val)

    for i_three in range(0,n-1):

        lista_u_i[i_three]=lista_v_i[i_three]

#print (len(lista_v_i))
#print (len(nova_u_i))
print (len(lista_u_i),lista_u_i)

#resultado analítico

def funcao_analitica(x,t):

    part_one = math.sin(math.pi*t)
    exponent = ((-1)*((math.pi**2)*t))
    part_two = 2.71**exponent

    return part_two*part_one

print (funcao_analitica(10,10))
