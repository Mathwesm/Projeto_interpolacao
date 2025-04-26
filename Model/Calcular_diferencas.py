import numpy as np


def calcular_diferencas_divididas(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Os arrays x e y devem ter o mesmo tamanho.")
    if n == 0:
        raise ValueError("Nenhum ponto foi fornecido.")
    if len(set(x)) != n:
        raise ValueError("Os valores de x devem ser distintos.")
    
    coeficientes = np.copy(y).astype(float)
    
    for j in range(1, n):
        coeficientes[j:n] = (coeficientes[j:n] - coeficientes[j-1:n-1]) / (x[j:n] - x[0:n-j])
    
    return coeficientes