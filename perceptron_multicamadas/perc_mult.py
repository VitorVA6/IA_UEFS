import math
from random import random
import numpy as np 
import random

def read_file():
    file = open('dataset/iris-10-1tra.dat', 'r')
    dados = file.read().split('\n')[9:]
    dados = [item.split(', ') for item in dados]
    x = [list(map(float, item[0:4])) for item in dados]
    for item in x:
        item.insert(0, -1)
    x = np.array(x)
    d = np.array([item[4] for item in dados])
    return x, d

def trainning():
    w_1 = np.array([[random.random() for _ in range(5)] for _ in range(2)])
    w_2 = np.array([random.random() for _ in range(3)])
    x, d = read_file()
    n = 0.1
    prec = 0.000001
    beta = 0.5
    epocas = 0
    eqm_ant = 100000
    eqm_atual = 0
    for xi, d in zip(x, d):
        i_1 = [sum(item) for item in w_1*xi]
        y_1 = [1/(1+math.exp(-beta*item)) for item in i_1]
        y_1.insert(0, -1)
        i_2 = sum(w_2*y_1)
        y_2 = 1/(1+math.exp(-beta*i_2))
        print(y_2)        

trainning()