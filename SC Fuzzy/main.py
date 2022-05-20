import numpy as np 
from matplotlib import pyplot as plt
from collections import defaultdict
import math

fator_temp = (1200-800)/499
temperatura = np.array([800+fator_temp*item for item in range(500)])

fator_vol = (12-2)/499
volume = np.array([2+fator_vol*item for item in range(500)])

fator_press = (12-4)/499
press = np.array([4+fator_press*item for item in range(500)])

temp_baixa = []
temp_media = []
temp_alta = []

for elem in temperatura:
    if elem <= 900:
        temp_baixa.append(1)
        temp_media.append(0)
        temp_alta.append(0)
    if elem > 900 and elem <= 1000:
        temp_baixa.append((1000-elem)/(1000-900))
        temp_media.append((elem-900)/(1000-900))
        temp_alta.append(0)
    if elem > 1000 and elem <= 1100:        
        temp_baixa.append(0)
        temp_media.append((1100-elem)/(1100-1000))
        temp_alta.append((elem-1000)/(1100-1000))
    if elem > 1100:
        temp_baixa.append(0)
        temp_media.append(0)
        temp_alta.append(1)

vol_peq = []
vol_medio = []
vol_gra = []

for elem in volume:
    if elem <= 4.5:
        vol_peq.append(1)
        vol_medio.append(0)
        vol_gra.append(0)
    if elem > 4.5 and elem <= 7:
        vol_peq.append((7-elem)/(7-4.5))
        vol_medio.append((elem-4.5)/(7-4.5))
        vol_gra.append(0)
    if elem > 7 and elem <= 9.5:        
        vol_peq.append(0)
        vol_medio.append((9.5-elem)/(9.5-7))
        vol_gra.append((elem-7)/(9.5-7))
    if elem > 9.5:
        vol_peq.append(0)
        vol_medio.append(0)
        vol_gra.append(1)

press_baixa = []
press_media = []
press_alta = []

for elem in press:
    if elem <= 5:
        press_baixa.append(1)   
        press_alta.append(0) 
    if elem > 5 and elem <= 8:
        press_baixa.append((8-elem)/(8-5))
        press_alta.append(0) 
    if elem > 8 and elem <= 11:
        press_baixa.append(0)
        press_alta.append((elem-8)/(11-8)) 
    if elem > 11:
        press_baixa.append(0)
        press_alta.append(1) 

for elem in press:
    if elem <= 6 or elem >= 10:
        press_media.append(0)
    if elem > 6 and elem <= 8:
        press_media.append((elem-6)/(8-6))
    if elem > 8 and elem < 10:
        press_media.append((10-elem)/(10-8))

regras = [
    [temp_baixa, vol_peq, press_baixa],
    [temp_media, vol_peq, press_baixa],
    [temp_alta, vol_peq, press_media],
    [temp_baixa, vol_medio, press_baixa],
    [temp_media, vol_medio, press_media],
    [temp_alta, vol_medio, press_alta],
    [temp_baixa, vol_gra, press_media],
    [temp_media, vol_gra, press_alta],
    [temp_alta, vol_gra, press_alta],
    ]

def closest(lst, K):
     lst = np.asarray(lst) 
     idx = (np.abs(lst - K)).argmin() 
     return idx

def alpha_corte(corte, vet):
    def apply(x):
        if x > corte:
            x = corte
        return x
    return map(apply, vet)

def centro_massa(vet):
    val_intervalo = []
    keys = defaultdict(list)
    for key, value in enumerate(vet):
        keys[value].append(key)
    for value in keys:
        if len(keys[value]) > 2:
            val_intervalo.append([value, [keys[value][0], keys[value][-1]]]) 
    val_inters = []
    for item in val_intervalo:
        inicio = math.ceil(press[item[1][0]]) 
        fim =  math.floor(press[item[1][1]]) 
        val_inters.append([item[0], list(range(inicio, fim+1))])
    numerador = sum([item[0]*sum(item[1]) for item in val_inters])
    denominador = sum([item[0]*len(item[1]) for item in val_inters])
    print(numerador/denominador)

saidas = []

for regra in regras:
    A = regra[0][closest(temperatura, 965)]
    B = regra[1][closest(volume, 11)]
    corte = min(A, B)
    saidas.append(list(alpha_corte(corte, regra[2])))

saidas = np.array(saidas)

agregado = [max(saidas[0:, item]) for item in range(500)]

centro_massa(agregado)
plt.plot(press, np.array(agregado))
plt.show()