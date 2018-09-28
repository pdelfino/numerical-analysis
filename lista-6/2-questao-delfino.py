import numpy as np
import matplotlib.pyplot as plt

def y_t_plus_h(h,y):

    return y/(1+10*h)

def implicit_euler(y_t_plus_h,h, interval):
    
    x_init = 0
    y_init = 1
    
    old_y = y_init
    old_t = x_init
    
    new_t = []
    new_t.append(old_t)

    new_y = []
    new_y.append(old_y)
    
    while old_t < interval[1]:
        
        y = y_t_plus_h(h, old_y)
        new_y.append(y)
        new_t.append(old_t+h) 
        old_y = y
        old_t = old_t + h
    
    return new_t, new_y

interval = [0,5]

print ((implicit_euler(y_t_plus_h,0.1,interval))[1])


