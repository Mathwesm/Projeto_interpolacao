import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Model.interpolacao_newton import interpolacao_newton
from Model.plotar_interpolacao import plotar_interpolacao
from Model.pontos_proximos import selecionar_pontos_mais_proximos


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
        
        quantidade = int(input("Quantos pontos você quer usar para interpolar? (Ex: 3 para grau 2) "))
        if quantidade <= 1 or quantidade > n:
            raise ValueError("Quantidade de pontos para interpolação inválida.")
        
        pontos_selecionados = selecionar_pontos_mais_proximos(pontos, x_interpolar, quantidade)
        pontos_selecionados.sort()
        
        resultado, coeficientes = interpolacao_newton(pontos_selecionados, x_interpolar)
        
        print(f"\nValor interpolado em x = {x_interpolar}: {resultado:.6f}")
        print("\nCoeficientes das diferenças divididas:")
        for i, coef in enumerate(coeficientes):
            print(f"  c[{i}] = {coef:.6f}")
        
        plotar_interpolacao(pontos_selecionados, coeficientes)
    
    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
