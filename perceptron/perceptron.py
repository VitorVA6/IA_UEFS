import random
import numpy as np

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

def perceptron():
    w = np.array([random.random() for item in range(0,4)])
    print(w)
    n = 0.01
    dados = read_file()
    x = np.array([item[0:4] for item in dados])
    d = np.array([item[4] for item in dados])
    epocas = 0
    while True:
        erros = 0
        for xi, di in zip(x, d):
            u = sum(xi*w)
            y = f_u(u)
            if(y != di):
                w = w + n*(di-u)*xi
                erros+=1
        epocas +=1
        if erros==0:
            break
    print(w)
    print(epocas)
    print(teste(w))

perceptron()