import time

start_time = time.time()

def function_exercise_1(x):

    return (x**3)-(x)-2

a = function_exercise_1(1)
#print (function_exercise_1(1))

b = function_exercise_1(2)
#print (function_exercise_1(2))

intervalo = [1,2]

new_val = (a+b)/2


def bissection(interval,function):

    a = interval[0]
    #print ("a",a)
    
    b = interval[1]
    #print ("b", b)

    function_output_a = function(a) 
    #print ("function_output_a", function_output_a)

    function_output_b = function(b)
    #print ("function_output_b", function_output_b)

    new_input = (a + b)/2
    #print ("new_input", new_input)

    new_output = function(new_input)
    #print ("new_output", new_output)
    
    if new_output>0:

        interval[1]=new_input
    
        #print ("interval, apos alteracao", interval)

    elif new_output<0:

        interval[0]=new_input
        #print ("interval, apos alteracao", interval)


    abs_output = abs(new_output)
    #print ("abs_output", abs_output)

    if abs_output<0.0000000000000000000000000000001:

        #print ("root: ")
        return new_input

    elif new_val<0:
   
        return bissection(interval, function)
        
    elif new_val>0:

        return bissection(interval, function)

    else:

        return "error"

print (bissection(intervalo, function_exercise_1))

print ("Time to run: ", float(time.time() - start_time))
