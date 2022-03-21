import random
import numpy as np
from matplotlib import pyplot as plt

def f_u(u):
    if(u>=0.0):
        return 1
    else:
        return -1

def read_file():
    file = open('treinamento.txt', 'r')
    dados = file.read().split('\n')
    dados = [item.split(' ') for item in dados]
    dados = [list(map(float, item)) for item in dados]
    return dados

def teste(w):
    file = open('teste.txt', 'r')
    dados = file.read().split('\n')
    dados = [item.split(' ') for item in dados]
    dados = np.array([list(map(float, item)) for item in dados])
    lista_y=[]
    for xi in dados:
        y = f_u(sum(xi*w))
        lista_y.append(y)
    return lista_y

def adeline():
    erros = []
    epocas = 0
    prec = 0.000001
    n = 0.0025
    dados = read_file()
    w = np.array([random.random() for item in range(5)])
    print(w)
    x = np.array([item[0:5] for item in dados])
    d = np.array([item[5] for item in dados])
    eqm_ant = 100000
    eqm_atual = 1
    while (abs(eqm_atual - eqm_ant)>=prec):
        eqm_ant = eqm_atual
        lista_u = []
        for xi, di in zip(x, d):
            u = sum(xi*w)
            lista_u.append(u)
            w = w + n*(di-u)*xi
        eqm_atual = sum((d-lista_u)**2)*(1/35)
        erros.append(eqm_atual)
        epocas+=1
    print(w)
    print(epocas)
    print(teste(w))
    plt.plot(range(epocas), erros)
    plt.title('Treinamento 5')
    plt.xlabel('Epocas')
    plt.ylabel('EQM')
    plt.show()

adeline()