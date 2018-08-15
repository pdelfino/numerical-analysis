import unittest
import numpy as np
import copy
import random

example_A_matrix = [[2,1],[5,7]]

example_b = [[11], [13]]

#######################################

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

def iterative_jacobi(matrix, b):

    x_init = x_init_guess_dim(len(matrix))
    #print ("x_init", x_init)

    prev_value = x_init
    #print ("prev_value", prev_value)

    diff_x_val = 1
    #print ("diff_x_val", diff_x_val)

    count_iterations = 1
    while diff_x_val>0.00001:
        
        count_iterations += 1
        #print ("count_iterations ", count_iterations)

        new_value = jacobi(matrix, b, prev_value)
        #print ("new_value", new_value)

        diff_x_vector = np.subtract(prev_value, new_value)
        #print ("diff_x_vector", diff_x_vector)

        diff_x_val = abs(np.sum(diff_x_vector))

        #print ("diff_x_val", diff_x_val)

        prev_value = new_value
        #print ("final value", prev_value)

    return prev_value

# usar a implementação para o exemplo do wikipédia
#print (iterative_jacobi(example_A_matrix, example_b))

#######################################

#fazer a matriz do enunciado

teste = [[1,2,3],[4,5,6],[7,8,9]]

enunciado_matrix = make_squared_matrix(10)
#print (enunciado_matrix)

def make_enunciado_matrix(matrix):

    diagonal_ele = 0
    
    for row in matrix:
        
       #print ("row", row)

        for col in range(0,len(row)):
            
           #print ("col", col)

            if col==diagonal_ele:
                    
                sorteio = random.randint(400,801)

                matrix[diagonal_ele][diagonal_ele] = sorteio
       
       #print (diagonal_ele)
        diagonal_ele += 1

    return matrix

def make_vector_b(matrix):

    ref = len(matrix)

    vector_b = []

    for i in matrix:
        
        sorteado = random.randint(0,ref+1)

        vector_b.append([sorteado])

    return vector_b

print (make_vector_b(enunciado_matrix))
    
print (make_enunciado_matrix(enunciado_matrix))

#agora fazer com que 2% dos elementos, tirando os da diagonal, sejam entre 0 e 1.