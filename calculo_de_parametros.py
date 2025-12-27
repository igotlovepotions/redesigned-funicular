import numpy as np
import math
import cmath
from config import CABOS, FREQUENCIA, RESISTIVIDADE_SOLO, CONDUTOR_RMG, PARA_RAIO_RMG

def calcular_matrizes():
    # Identificar condutores
    nomes = list(CABOS.keys())
    n = len(nomes)
    
    # Prepara listas ordenadas para acesso por índice
    # É importante manter uma ordem consistente (ex: A, B, C, PR1)
    condutores = [CABOS[nome] for nome in nomes]
    
    # Matriz de Distâncias e Matriz L
    # Matriz Z (Impedância Longitudinal)
    # Z_ii = Ri + j*omega*kl * ln(De/RMG)
    # Z_ij = j*omega*kl * ln(De/Dij)
    
    omega = 2 * np.pi * FREQUENCIA
    
    # Constante de Carson para retorno pelo solo (aproximação)
    # De = 658.4 * sqrt(rho / f)
    De = 658.37 * math.sqrt(RESISTIVIDADE_SOLO / FREQUENCIA)
    
    # Matriz de impedância primitiva (Z_hat)
    # Vamos considerar apenas a parte reativa indutiva + correção de Carson simplificada por enquanto,
    # ou usar a formula completa se desejado. O código original usava log(DE/d).
    # Vamos seguir a linha do log(De/d) que é a aproximação de Carson para Indutância mútua.
    
    # Termo constante de indutância: 2e-7 H/m = 0.2 mH/km ? 
    # Formula usual: L = 2e-7 * ln(De/D) (H/m)
    # Para km: 2e-4 * ln(De/D) (H/km)
    
    # O código original não tinha as constantes, apenas log(DE/..). 
    # Vou aplicar a constante de permeabilidade para obter Henrys reais.
    mu0_2pi = 2e-7 # H/m
    
    L_matrix = np.zeros((n, n))
    
    # Matriz de Coeficientes de Potencial (para capacitância) - P_matrix
    # P_ij = (1 / (2*pi*epsilon0)) * ln(S_ij / D_ij)
    # Onde S_ij é a distância entre 'i' e a IMAGEM de 'j'.
    # D_ij é a distância direta.
    epsilon0 = 8.854e-12
    k_cap = 1 / (2 * np.pi * epsilon0) # ~ 1.797e10
    
    P_matrix = np.zeros((n, n))

    print(f"Calculando para {n} condutores: {nomes}")
    print(f"Profundidade de retorno de Carson (De): {De:.2f} m")

    for i in range(n):
        for j in range(n):
            # Coordenadas
            xi, yi = condutores[i]['x'], condutores[i]['y']
            xj, yj = condutores[j]['x'], condutores[j]['y']
            
            # Distância Geométrica (Dij)
            dx = xi - xj
            dy = yi - yj
            d_ij = math.sqrt(dx**2 + dy**2)
            
            # Distância para a Imagem (Sij)
            # Imagem de j está em (xj, -yj)
            dy_img = yi - (-yj) # yi + yj
            s_ij = math.sqrt(dx**2 + dy_img**2)
            
            # RMG ou Raio do condutor i
            if condutores[i]['tipo'] == 'para-raio':
                rmg_i = PARA_RAIO_RMG
                raio_i = PARA_RAIO_RMG # Aproximação se não tiver raio fisico separado
            else:
                rmg_i = CONDUTOR_RMG
                raio_i = CONDUTOR_RMG # ! ATENÇAO: Para capacitância usa-se o RAIO EXTERNO, para indutância o RMG.
                # No config atual temos CONDUTOR_RAIO_M disponivel, mas não importei acima.
                # Vamos simplificar e usar RMG por enquanto ou importar se for critico.
                # Vou usar RMG como fallback mas o ideal é raio geometrico.
            
            # --- Cálculo de L (Indutância) ---
            # Z = j*omega * 2e-7 * ln(De / D_eq)
            if i == j:
                # Auto-indutância
                termo_ln = math.log(De / rmg_i)
            else:
                # Indutância mútua
                termo_ln = math.log(De / d_ij)
            
            # L em H/m
            L_matrix[i, j] = 2e-7 * termo_ln
            
            # --- Cálculo de P (Potencial -> Capacitância) ---
            if i == j:
                # Auto-potencial: ln(2*h / r)
                # S_ii = 2*yi
                termo_p = math.log((2*yi) / raio_i)
            else:
                # Potencial mútuo: ln(S_ij / D_ij)
                termo_p = math.log(s_ij / d_ij)
                
            P_matrix[i, j] = k_cap * termo_p

    # Capacitância = Inversa de P
    try:
        C_matrix = np.linalg.inv(P_matrix)
    except np.linalg.LinAlgError:
        C_matrix = np.zeros_like(P_matrix)
        print("Erro: Matriz depotencial singular.")

    return nomes, L_matrix, C_matrix

if __name__ == "__main__":
    nomes, L, C = calcular_matrizes()
    print("\n--- Matriz de Indutância (H/m) ---")
    print(L)
    print("\n--- Matriz de Capacitância (F/m) ---")
    print(C)
