import unittest


example_A_matrix = [[2,1],[5,7]]

example_b = [11, 13]

def make_squared_matrix(n):

    squared_matrix = []

    lines = []

    for i in range(0, n):

        lines.append(0)

    for i in range(0,n):

        squared_matrix.append(lines[:])

    return squared_matrix

outra = [[1,2,3],[4,5,6],[7,8,9]]

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

    for linha in range(0,len(matrix)):
        for coluna in range(0,len(matrix)):
            
            if linha==coluna:
                matrix[linha][coluna]=0

    return matrix

print (get_diagonal(example_A_matrix))

print (get_rest(example_A_matrix))

"""
Pq caralhos para de funcionar o test case se eu adiciono um fucking print?

"""
##############################

class Test(unittest.TestCase):

    def test_squared(self):
        self.assertEqual(make_squared_matrix(3), [[0,0,0],[0,0,0],[0,0,0]])

    def test_get_diagonal(self):
        self.assertEqual(get_diagonal(example_A_matrix), [[2,0],[0,7]])

if __name__ == '__main__':
    unittest.main()

