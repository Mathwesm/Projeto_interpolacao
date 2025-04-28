
def polinomio_newton(x_valores, coeficientes, x):
    n = len(coeficientes)
    if n == 0:
        raise ValueError("Nenhum coeficiente foi fornecido.")
    
    resultado = coeficientes[-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x_valores[i]) + coeficientes[i]
    return resultado