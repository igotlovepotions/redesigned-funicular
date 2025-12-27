import cmath
import math as mt

## Valores iniciais
frequencia = 60  ## Hz
omega = 2 * mt.pi * frequencia  ## ~377 rad/s
tensao = 500  ## kV (Tensão de linha)

## Valores iniciais de R L C (por km)
resistencia_feixe = 0.0733  ## ohms/km
resistencia = resistencia_feixe / 4
indutancia = 0.746e-3       ## Convertido para H/km (mH -> H)
capacitancia = 14.88e-9     ## Convertido para F/km (nF -> F)
G = 0                       ## Condutância (geralmente desprezada ou zero)
j = complex(0, 1)           ## Unidade imaginária

### Começo dos cálculos

# 1. Impedância de surto (sem perdas)
Zs = mt.sqrt(indutancia / capacitancia)

# 2. Impedância característica (com perdas)
# Z = R + jwL | Y = G + jwC
Z_serie = resistencia + j * omega * indutancia
Y_shunt = G + j * omega * capacitancia
Zc = cmath.sqrt(Z_serie / Y_shunt)

# 3. Velocidade de propagação (aprox. 1/sqrt(LC))
velocidade = 1 / mt.sqrt(indutancia * capacitancia)

# 4. Comprimento de onda (lambda)
lambda_onda = velocidade / frequencia

# 5. Potência Natural (SIL) = V^2 / Zc
# Usamos a magnitude de Zc para o cálculo de potência
potencia_natural = (tensao**2) / abs(Zc) 

# 6. Constante de propagação (gamma)
gama = cmath.sqrt(Z_serie * Y_shunt)

## Exibição de resultados (Exemplos)
