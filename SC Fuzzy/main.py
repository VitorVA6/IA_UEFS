import numpy as np 

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

def closest(lst, K):
     lst = np.asarray(lst) 
     idx = (np.abs(lst - K)).argmin() 
     return idx

A = temp_baixa[closest(temperatura, 965)]
B = vol_peq[closest(volume, 11)]

print(press_media)