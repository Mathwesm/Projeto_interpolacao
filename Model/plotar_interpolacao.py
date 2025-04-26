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
    plt.scatter(x_valores, y_valores, color='red', label='Pontos dados', zorder=5)
    plt.title('Interpolação de Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    backend = plt.get_backend()
    if 'agg' in backend.lower():
        plt.savefig('/home/matheus/Documentos/Trabalhos/Projeto_interpolação/View/interpolacao_newton.png')
        print("\nAviso: Ambiente não suporta exibição interativa de gráficos.")
        print("Gráfico salvo como 'interpolacao_newton.png' na pasta View.")
    else:
        plt.show()