import math

def f(x):

    return (math.e)**x

#print (f(1))

def euler(dx,x):
    
    x_init = 0
    
    y_init = 1
    
    old_dy_dx = y_init

    old_y = y_init 

    new_y = None
    
    new_dy_dx = None

    delta_x = dx
    
    limite = 0

    while x>limite:

        #for i in range(1,6):
        
        new_y = delta_x*old_dy_dx + old_y
        #print ("new_y", new_y)

        new_dy_dx = new_y
        #print ("new dy_dx", new_dy_dx)

        old_y = new_y
        #print ("old_y", old_y)

        old_dy_dx = new_y
        #print ("old delta y_delta x", old_dy_dx)
        #print ("iterada",i)
        
        limite = limite +dx

    return new_y

print (euler(0.0000001,25))


