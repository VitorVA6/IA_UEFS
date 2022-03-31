import math
from random import random
import numpy as np 
import random
import glob

def read_file(name_file):
    file = open(name_file, 'r')
    dados = file.read().split('\n')[9:]
    dados = [item.split(', ') for item in dados]
    x = [list(map(float, item[0:4])) for item in dados]
    for item in x:
        item.insert(0, -1)
    x = np.array(x)
    d = []
    for item in dados:
        if item[4].strip() == 'Iris-setosa':
            d.append([1, 0])
        elif item[4].strip() == 'Iris-versicolor':
            d.append([0, 1])
        elif item[4].strip() == 'Iris-virginica':
            d.append([0, 0])
    d = np.array(d)
    return x, d

def g_u(i, beta):
    return [1/(1+math.exp(-beta*item)) for item in i]

def trainning(file_name):
    w_1 = np.array([[random.random() for _ in range(5)] for _ in range(10)])
    w_1_ant = w_1
    w_2 = np.array([[random.random() for _ in range(11)] for _ in range(2)])
    w_2_ant = w_2
    x, d = read_file(file_name)
    n = 0.1
    prec = 0.000001
    beta = 0.5
    alpha = 0
    epocas = 0
    eqm_ant = 100000
    eqm_atual = 0
    while (abs(eqm_atual - eqm_ant)>=prec):
        eqm_ant = eqm_atual
        erros = []
        for xi, di in zip(x, d):
            i_1 = [sum(item) for item in w_1*xi]
            y_1 = g_u(i_1 ,beta)
            y_1.insert(0, -1)
            y_1 = np.array(y_1)
            i_2 = [sum(item) for item in w_2*y_1]
            y_2 = np.array(g_u(i_2, beta))
            g_2 = np.array([(di-y_2)*beta*y_2*(1-y_2)])
            aux_2 = w_2
            w_2 = w_2 + n*g_2.T*y_1 + alpha*(w_2 - w_2_ant)
            w_2_ant = aux_2
            func = np.array(g_u(i_1, beta))
            g_1 = np.array([sum(w_2[0:, 1:]*g_2.T)*beta*func*(1-func)])
            aux_1 = w_1
            w_1 = w_1 + n*g_1.T*xi + alpha*(w_1 - w_1_ant)
            w_1_ant = aux_1
            erros.append((1/2)*sum((di-y_2)**2))
        eqm_atual = sum(erros)*(1/len(erros))
        epocas += 1

    return w_1, w_2, epocas, eqm_atual

def test(w_1, w_2, file_name):
    x, d = read_file(file_name)
    beta = 0.5
    acertos = 0
    for xi, di in zip(x, d):
        i_1 = [sum(item) for item in w_1*xi]
        y_1 = g_u(i_1 ,beta)
        y_1.insert(0, -1)
        y_1 = np.array(y_1)
        i_2 = [sum(item) for item in w_2*y_1]
        y_2 = np.around(g_u(i_2, beta))
        if np.array_equal(y_2, di):
            acertos+=1

    acuracia = (acertos/len(d))*100
    return acuracia

file_names = glob.glob('dataset/*')
lista_epocas = []
lista_eqm = []
lista_acuracia = []

for pos in range(10):
    w_1, w_2, epocas, eqm = trainning(file_names[pos*2])
    acuracia = test(w_1, w_2, file_names[pos*2 + 1])
    lista_epocas.append(epocas)
    lista_eqm.append(eqm)
    lista_acuracia.append(acuracia)
    print('Parte '+str(pos+1) + '/10 concluída...')

print('\n Resultados das médias: \n')
print('Épocas: ' + str(sum(lista_epocas)/len(lista_epocas)))
print('Eqm: ' + str(sum(lista_eqm)/len(lista_eqm)))
print('Acurácia: ' + str(sum(lista_acuracia)/len(lista_acuracia)))
print('\n Resultados do desvio padrão: \n')
print('Épocas: ' + str(np.std(lista_epocas)))
print('Eqm: ' + str(np.std(lista_eqm)))
print('Acurácia: ' + str(np.std(lista_acuracia)))