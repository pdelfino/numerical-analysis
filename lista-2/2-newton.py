import time
start_time = time.time()

#######################################
def wikipedia_function(x):

    return x**2-612

def derivative_wikipedia_function(x):

    return 2*x

#######################################

def function_exercise_2(x):

    return (x**3)-x-2

#print (function_exercise_2(1))

def derivative_function_exercise_2(x):

    return 3*(x**2)-1

#print (derivative_function_exercise_2(1))


def newton_method(x_zero,f,f_linha):

    x_one = x_zero - (f(x_zero)/f_linha(x_zero))
    
    return x_one

def iterative_newton_method(x_zero,f,f_linha):

    x = newton_method(x_zero,f,f_linha)

    x_plus_1 = newton_method(x,f,f_linha)
   
    diff = abs(x_plus_1 - x)
    print ("x",x,"x_plus_1",x_plus_1,"diff", diff)
    
    counter = 1
    
    while diff>0.00001:

        x = x_plus_1
        print ("x", x)
        
        counter += 1
        print (counter)
        
        x_plus_1 = newton_method(x,f, f_linha)
        print ("x_plus_1", x_plus_1)
        
        diff = abs(x_plus_1-x)
        print ("diff", diff) 

    return x

#print (iterative_newton_method(1, wikipedia_function, derivative_wikipedia_function))
print (iterative_newton_method(10, function_exercise_2, derivative_function_exercise_2))

print ("time to run: ", time.time() - start_time)
