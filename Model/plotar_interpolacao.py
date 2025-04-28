import matplotlib.pyplot as plt
import numpy as np
from Model.Polinomio_newton import polinomio_newton

def plotar_interpolacao(pontos, coeficientes):
    x_valores, y_valores = zip(*pontos)
    x_valores = np.array(x_valores)
    
    x_range = max(x_valores) - min(x_valores)
    x_plot = np.linspace(min(x_valores) - 0.1 * x_range, max(x_valores) + 0.1 * x_range, 500)
    y_plot = [polinomio_newton(x_valores, coeficientes, xi) for xi in x_plot]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, label='Polinômio de Newton', color='blue')
    plt.scatter(x_valores, y_valores, color='red', label='Pontos usados', zorder=5)
    plt.title('Interpolação de Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    try:
        plt.show()
    except:
        print("\nAviso: O ambiente não suporta exibição interativa de gráficos.")
        plt.savefig('interpolacao_newton.png')
        print("Gráfico salvo como 'interpolacao_newton.png' na pasta atual.")