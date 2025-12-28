import numpy as np
from calculo_de_parametros import calcular_matrizes
from mostrar_cabos import plotar_geometria
import sys

def main():
    print("=== Redesigned Funicular - Cálculo de Parâmetros de LT ===")
    
    # 1. Mostrar Geometria (Perguntar ou mostrar direto? Vamos mostrar direto por enquanto)
    print("Gerando gráfico da torre...")
    # Comentado para execução em ambiente headless se necessário, mas o user pediu "fazer o 1, 2, 3"
    # Se o user tiver display, vai abrir a janela.
    try:
        fig = plotar_geometria()
        # Se estiver rodando interativamente via terminal, plt.show() seria chamado dentro de plotar_geometria
        # mas agora ela retorna a figura.
        import matplotlib.pyplot as plt
        plt.show()
    except Exception as e:
        print(f"Não foi possível plotar a geometria (sem display?): {e}")

    # 2. Calcular Matrizes
    print("\nCalculando parâmetros elétricos...")
    nomes, L_mat, C_mat = calcular_matrizes()
    
    # 3. Exibir Resultados de forma legível
    print("\n" + "="*50)
    print("RESULTADOS (Valores por metro)")
    print("="*50)
    
    # Formatação bonita com numpy
    np.set_printoptions(precision=4, linewidth=150, suppress=True)
    
    print(f"\nCondutores: {nomes}")
    
    print("\n[L] Matriz de Indutância (micro H/m):")
    print((L_mat * 1e6)) 
    
    print("\n[C] Matriz de Capacitância (pico F/m):")
    print((C_mat * 1e12))
    
    print("\n" + "="*50)
    
    # Redução de Kron (Exemplo simples: eliminando para-raios se houver)
    # Supondo que os últimos sejam para-raios (terra)
    # Essa implementação é genérica, apenas um placeholder para expansão futura
    # Se PR1 for aterrado, V_pr1 = 0.
    
    print("\nNota: Os valores acima consideram a matriz primitiva completa.")
    print("Para parâmetros de sequência, seria necessário realizar a redução de Kron")
    print("eliminando os cabos para-raios (aterrados).")

if __name__ == "__main__":
    main()
