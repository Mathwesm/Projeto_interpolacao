import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.interpolacao_newton import interpolacao_newton
from Model.plotar_interpolacao import plotar_interpolacao

def main():
    print("=== Interpolação de Newton ===")
    
    try:
        n = int(input("Quantos pontos você quer inserir? "))
        if n <= 0:
            raise ValueError("O número de pontos deve ser positivo.")
        
        pontos = []
        for i in range(n):
            x = float(input(f"Digite o valor de x[{i}]: "))
            y = float(input(f"Digite o valor de y[{i}]: "))
            pontos.append((x, y))
        
        x_interpolar = float(input("Digite o valor de x que deseja interpolar: "))
        
        resultado, coeficientes = interpolacao_newton(pontos, x_interpolar)
        
        print(f"\nValor interpolado em x = {x_interpolar}: {resultado:.6f}")
        print("Coeficientes das diferenças divididas:")
        for i, coef in enumerate(coeficientes):
            print(f"  c[{i}] = {coef:.6f}")
        
        plotar_interpolacao(pontos, coeficientes)
    
    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()