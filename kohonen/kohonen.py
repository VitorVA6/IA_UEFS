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

def kohonen():
    x = read_file('dataset/iris-10-1tra.dat')
    w = np.array([[[random.random() for _ in range(5)] for _ in range(5)]for _ in range(5)])
    vizinhos = [[[0, 1], [1, 0]] ,[[0, 0], [1, 1], [2, 0]]]
    print(w)

def vizinhos():
    viz = []
    for l in range(5):
        for c in range(5):
            viz.append([[l, c+1], [l,c-1], [l+1, c], [l-1, c]])
    viz = np.array(viz)
    indices = np.where(viz==-1)[0]
    indices2 = np.where(viz==-1)[1]
    viz = np.delete(viz, )
    

vizinhos()