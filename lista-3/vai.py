def generate_pol(M, pontos):
    
    """
    Gera o polinômio a partir da matriz das diferenças divididas e os pontos dados.
    
    :param M: matriz das diferenças divididas
    :param pontos: lista com n pontos (x, y)
    
    :return: polinômio interpolador
    """

    x = sp.Symbol('x')

    values = [i[0] for i in pontos]

    prod = 1
    exp = M[0][0] # Define c_0

    for i in range(len(M)-1): # Demais termos do polinômio

        prod = prod*(x - values[i])
        exp = exp + M[0][i+1]*prod
        
    exp = sp.simplify(exp)

    return exp

def interpol_dif_div(pontos):
    
    """
    Obtém o polinômio interpolador dos pontos através do método das diferenças divididas.
    
    :param pontos: lista com n pontos (x,y)
    
    :returns: polinômio interpoladro
    """
    
    y = [i[1] for i in pontos]
    x = [i[0] for i in pontos]
    
    M = np.identity(len(x))
    
    # Calcula a matriz das diferencas divididas 
    
    for j in range(len(x)): # Fixa a coluna
        for i in range(len(x), -1, -1): # Sobe nas linhas da matriz
            
            if i == j:
                M[i][j] = y[i] # [y_i] =  y_i
                
            elif j > i:

                M[i][j] = (M[i+1][j] - M[i][j-1])/(x[j]-x[i])
        
    print('Matriz das diferenças divididas:\n', M)
    exp = generate_pol(M, pontos)
    
    return exp
