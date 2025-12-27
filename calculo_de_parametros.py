from show_cables import cables 
import math as mt 
import cmath
import numpy as np

##definiicsoa dimensoes do condutor e feixe
distancia_feixe = 0.457 # m 
condutor_diametro = 29.59 ## mm 
condutor_raio = condutor_diametro / 2
condutor_rmg = 1.09 *  (condutor_raio * distancia_feixe**3)**0.25

##defiinindo para-raio

para_raio_rmg = 30.35E-12 ## m


## usa-se o metodo do condutor pelo solo 

##DE = 658.37 * math.sqrt ( res / freq) freq = 60 hz , res = resistividade do solo, 100 ohms
DE = 849.95
##primeira matriz 

## indutancia



#calcular as distancias d


dab
dac
dapr1
dapr2
dba 
dbc
dbpr1
dbpr2
dca
dcb 
dcpr1
dcpr2

## usa-se o metodo do condutor pelo solo 

## DE = 658.37 * math.sqrt ( res / freq) freq = 60 hz , res = resistividade do solo, 100 ohms

##primeira matriz 

## indutancia
 
matriz_indutancia = [
    [mt.log(DE / condutor_rmg), mt.log(DE / dab)         , mt.log(DE / dba)         , mt.log(DE / dca)]
    [mt.log(DE / dab)         , mt.log(DE / condutor_rmg), mt.log(DE / dbc)         , mt.log(DE / dcb) ]
    [mt.log(DE / dac)         , mt.log(DE / dab)         , mt.log(DE / condutor_rmg), mt.log(DE / dcpr1) ]
    [mt.log(DE / dapr1)       , mt.log(DE / dab)         , mt.log(DE / dac)         , mt.log(DE / para_raio_rmg) ]

]


 






