import math

def f(x):

    return (math.e)**x

#print (f(1))

def euler(x,y_init):
    
    x_init = 1
    
    old_dy_dx = 1+(y_init**2)+(x_init**3)

    old_y = y_init 

    new_y = None
    
    new_dy_dx = None

    delta_x = 0.01
    
    limite = 0
    
    counter = 0
    while x>=limite:
        
        counter+=1
        print ("iterada",counter)
        #for i in range(1,6):
        
        new_y = (delta_x*old_dy_dx) + old_y
        print ("new_y", new_y,"old_y",old_y, "delta_x",delta_x, "old_dy_dx",old_dy_dx)

        new_dy_dx = 1+(new_y**2)+(delta_x**3)
        print ("new dy_dx", new_dy_dx)

        old_y = new_y
        print ("old_y", old_y)

        old_dy_dx = new_dy_dx
        print ("old delta y_delta x", old_dy_dx)
        
        limite = limite +delta_x

    return new_y

#print ("função analítica f(x)=e^x com input x=25: ", f(25))
#print ("função de aproximação numérica euleriana com input x=25: ", euler(2,4))
#print ("conclusão: a aproximação é muito boa")
print (euler(2,-4))
