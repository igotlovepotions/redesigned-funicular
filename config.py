
# Dados geométricos e físicos do sistema

# Constantes Físicas
FREQUENCIA = 60  # Hz
RESISTIVIDADE_SOLO = 100  # ohms
# Diâmetro e RMG (Raio Médio Geométrico)
# Valores originais do script
CONDUTOR_DIAMETRO_MM = 29.59
CONDUTOR_RAIO_M = (CONDUTOR_DIAMETRO_MM / 2) / 1000
DISTANCIA_FEIXE_M = 0.457

# Calculation of RMG for the bundle (assuming bundle of 2 based on previous logic, or adapting)
# Note: The original script used a specific formula 1.09 * (r * d^3)^0.25 - check if this is for 4 conductors?
# For now preserving the formula logic or simplifying. 
# Let's keep the user's specific RMG formula but parameterize it.
def calcular_rmg_feixe(raio_m, dist_feixe_m):
    # Formula from original script: 1.09 *  (condutor_raio * distancia_feixe**3)**0.25
    return 1.09 * (raio_m * dist_feixe_m**3)**0.25

CONDUTOR_RMG = calcular_rmg_feixe(CONDUTOR_RAIO_M, DISTANCIA_FEIXE_M)
PARA_RAIO_RMG = 30.35e-12 # conforme original (parece muito pequeno, mas mantendo)

# Resistência (Ohms/km)
RESISTENCIA_FEIXE = 0.0733
RESISTENCIA_EQUIV = RESISTENCIA_FEIXE / 4 # assumindo 4 subcondutores pelo divisor?

# Posições dos cabos (x, y)
# x = distância horizontal do centro
# y = altura do solo
CABOS = {
    'A':   {'x': -5, 'y': 28, 'tipo': 'fase'},
    'B':   {'x': 0,  'y': 34, 'tipo': 'fase'},
    'C':   {'x': 5,  'y': 28, 'tipo': 'fase'},
    'PR1': {'x': 0,  'y': 39, 'tipo': 'para-raio'},
    # 'PR2': {'x': 7, 'y': 30, 'tipo': 'para-raio'}, # Comentado no original
}
