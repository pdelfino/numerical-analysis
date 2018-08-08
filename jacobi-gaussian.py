import unittest
import numpy as np
import copy

example_A_matrix = [[2,1],[5,7]]

example_b = [[11], [13]]

def make_squared_matrix(n):

    squared_matrix = []

    for i in range(0,n):
        
        lines_list = []    
    
        for i in range(0,n):
            
            lines_list.append(0)
        
        squared_matrix.append(lines_list)

    return squared_matrix

def x_init_guess_dim(n):

    x_init = []
    
    for i in range(0,n):
        
        x_init.append([1])

    return x_init

x_init = x_init_guess_dim(2)

def get_diagonal(matrix):

    diagonal_matrix = make_squared_matrix(len(matrix))

    diagonal_val = []

    for i in range(0,len(matrix)):
        diagonal_val.append(matrix[i][i])

    counter = 0

    for linha in diagonal_matrix:
        diagonal_matrix[counter][counter]=diagonal_val[counter]

        counter += 1

    return diagonal_matrix

def get_rest(matrix):

    rest_matrix = copy.deepcopy(matrix)

    for linha in range(0,len(rest_matrix)):
        for coluna in range(0,len(rest_matrix)):
            
            if linha==coluna:
                rest_matrix[linha][coluna]=0

    return rest_matrix

def inverse_diagonal(matrix):

    diagonal = get_diagonal(matrix)

    inv = np.linalg.inv(diagonal)

    return inv

#print (inverse_diagonal(example_A_matrix))

def jacobi(matrix,b,x):

    D = get_diagonal(matrix)

    R = get_rest(matrix)

    D_inverse = inverse_diagonal(D)

    R_dot_x = np.matmul(R,x)

    b_minus = np.subtract(b,R_dot_x)

    x_iter = np.matmul(D_inverse,b_minus)

    return x_iter

a = jacobi(example_A_matrix,example_b,x_init)
print (a)

b = jacobi(example_A_matrix,example_b, a)
print (b)

c = jacobi(example_A_matrix, example_b, b)
print (c)

d = jacobi(example_A_matrix, example_b, c)
print (d)

prev_value = x_init

for i in range(0,55):

    new_value = jacobi(example_A_matrix, example_b, prev_value)

    prev_value = new_value

print (prev_value)
