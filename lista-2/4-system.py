import numpy as np

#### example from youtube https://www.youtube.com/watch?v=zPDp_ewoyhM

def jacobian_example(x,y):

    return [[1,2],[2*x,8*y]]

def function_example(x,y):
    
    return [(-1)*(x+(2*y)-2),(-1)*((x**2)+(4*(y**2))-4)]

def x_delta_by_gauss(J,b):

    return np.linalg.solve(J,b)

def x_plus_1(x_delta,x_previous):

    x_next = x_previous + x_delta
    
    return x_next

def newton_method(x_init):

    first = x_init[0]
    
    second = x_init[1]

    jacobian = jacobian_example(first, second)
    
    vector_b_f_output = function_example(first, second)

    x_delta = x_delta_by_gauss(jacobian, vector_b_f_output)

    x_plus_1 = x_delta + x_init

    return x_plus_1

counter = 0

x_old = [1,2]
print ("x_old", x_old)

x_new = newton_method(x_old)
print ("x_new", x_new)

diff = np.linalg.norm(x_old-x_new)
print (diff)

while diff>0.000000000000000000000000000000000001:

    counter += 1

    print ("x_old", x_old)
    x_new = newton_method(x_old)
    print ("x_new", x_new)
    
    diff = np.linalg.norm(x_old-x_new)
    print (diff)

    x_old = x_new

def iterative_newton(x_init):

    counter = 0

    x_old = x_init
    print ("x_old", x_old)

    x_new = newton_method(x_old)
    print ("x_new", x_new)

    diff = np.linalg.norm(x_old-x_new)
    print (diff)

    while diff>0.000000000000000000000000000000000001:

        counter += 1

        print ("x_old", x_old)
        x_new = newton_method(x_old)
        print ("x_new", x_new)
        
        diff = np.linalg.norm(x_old-x_new)
        print (diff)

        x_old = x_new

    convergent_val = x_new
    print (counter)
    
    return convergent_val

print (iterative_newton([1,2]))

