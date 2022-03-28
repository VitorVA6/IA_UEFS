import math
from random import random
import numpy as np 
import random

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
        if item[4] == 'Iris-setosa':
            d.append([1, 0, 0])
        elif item[4] == 'Iris-versicolor':
            d.append([0, 1, 0])
        elif item[4] == 'Iris-virginica':
            d.append([0, 0, 1])
    d = np.array(d)
    return x, d

def g_u(i, beta):
    return [1/(1+math.exp(-beta*item)) for item in i]

def trainning():
    w_1 = np.array([[random.random() for _ in range(5)] for _ in range(6)])
    w_2 = np.array([[random.random() for _ in range(7)] for _ in range(3)])
    x, d = read_file('dataset/iris-10-1tra.dat')
    n = 0.1
    prec = 0.000001
    beta = 0.5
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
            w_2 = w_2 + n*g_2.T*y_1
            func = np.array(g_u(i_1, beta))
            g_1 = np.array([sum(w_2[0:, 1:]*g_2.T)*beta*func*(1-func)])
            w_1 = w_1 + n*g_1.T*xi
            erros.append((1/2)*sum((di-y_2)**2))
        eqm_atual = sum(erros)*(1/len(erros))
        epocas += 1
    print(epocas)
    return w_1, w_2

def test(w_1, w_2):
    x, d = read_file('dataset/iris-10-1tst.dat')
    beta = 0.5
    for xi, di in zip(x, d):
        i_1 = [sum(item) for item in w_1*xi]
        y_1 = g_u(i_1 ,beta)
        y_1.insert(0, -1)
        y_1 = np.array(y_1)
        i_2 = [sum(item) for item in w_2*y_1]
        y_2 = np.array(g_u(i_2, beta))
        print(y_2)

w_1, w_2 = trainning()
test(w_1, w_2)
