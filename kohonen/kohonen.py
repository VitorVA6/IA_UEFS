import math
import random
import numpy as np 
import glob

def read_file(name_file):
    file = open(name_file, 'r')
    dados = file.read().split('\n')[9:]
    dados = [item.split(', ') for item in dados]
    x = [list(map(float, item[0:4])) for item in dados]
    for item in x:
        item.insert(0, -1)
    x = np.array(x)
    return x

def vizinhos():
    viz = []
    for l in range(5):
        for c in range(5):
            viz.append([[l,c-1], [l, c+1] ,  [l-1, c], [l+1, c]])   
    for e in viz:
        for el in e:
            if(-1 in el):
                indice1 = viz.index(e)
                indice2 = e.index(el)
                del(viz[indice1][indice2])
    for e in viz:
        for el in e:
            if 5 in el:
                indice1 = viz.index(e)
                indice2 = e.index(el)
                del(viz[indice1][indice2])
    return viz

def kohonen():
    x = read_file('dataset/iris-10-1tra.dat')
    w = np.array([[[random.random() for _ in range(5)] for _ in range(5)]for _ in range(5)])
    vizinhanca = vizinhos()
    n = 0.01
    epocas = 0

def teste():
    lista = [5, 0]
    if 5 in lista:
        print('tem')

kohonen()