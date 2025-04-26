import numpy as np
from Model.Calcular_diferencas import calcular_diferencas_divididas
from Model.Polinomio_newton import polinomio_newton

def interpolacao_newton(pontos, x_interpolar):

    if not pontos:
        raise ValueError("Nenhum ponto foi fornecido.")
    
    x_valores, y_valores = zip(*pontos)
    x_valores = np.array(x_valores)
    y_valores = np.array(y_valores)
    
    coeficientes = calcular_diferencas_divididas(x_valores, y_valores)
    resultado = polinomio_newton(x_valores, coeficientes, x_interpolar)
    
    return resultado, coeficientes