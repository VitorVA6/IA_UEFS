import math
import random
import numpy as np 
import glob

dim = 10

def read_file(name_file):
    file = open(name_file, 'r')
    dados = file.read().split('\n')[9:]
    dados = [item.split(', ') for item in dados]
    x = np.array([list(map(float, item[0:4])) for item in dados])
    x[0:, 0] = normalize(x[0:, 0], 4.3, 7.9)
    x[0:, 1] = normalize(x[0:, 1], 2.0, 4.4)
    x[0:, 2] = normalize(x[0:, 2], 1.0, 6.9)
    x[0:, 3] = normalize(x[0:, 3], 0.1, 2.5)
    return x

def normalize(arr, minimo, maximo):
    norm_arr = []
    diff_arr = maximo - minimo    
    for i in arr:
        temp = ((i - minimo)/diff_arr)
        norm_arr.append(temp)
    return np.array(norm_arr)

def vizinhos():
    viz = []
    for l in range(dim):
        for c in range(dim):
            viz.append([[l,c-1], [l, c+1] ,  [l-1, c], [l+1, c]])   
    for e in viz:
        for el in e:
            if(-1 in el):
                indice1 = viz.index(e)
                indice2 = e.index(el)
                del(viz[indice1][indice2])
    for e in viz:
        for el in e:
            if dim in el:
                indice1 = viz.index(e)
                indice2 = e.index(el)
                del(viz[indice1][indice2])
    return viz

def kohonen():
    x = read_file('dataset/iris-10-1tra.dat')
    w = np.array([[[random.random() for _ in range(4)] for _ in range(dim)]for _ in range(dim)])
    vizinhanca = vizinhos()
    n = 0.01
    epocas = 0
    menor = [100, 0, 0]
    menor_aux = [0, 0, 0]
    while menor_aux[0] != menor[0]:
        menor_aux = menor
        for xi in x:
            menor = [100, 0, 0]
            for l in range(dim):
                for c in range(dim):
                    norm = np.linalg.norm(xi-w[l][c])
                    if norm < menor[0]:
                        menor = [norm, l, c]
            
            vizinhos_menor = vizinhanca[menor[1]*dim + menor[2]]
            w[menor[1]][menor[2]] = w[menor[1]][menor[2]] + n*(xi - w[menor[1]][menor[2]])
            for e in vizinhos_menor:
                w[e[0]][e[1]] = w[e[0]][e[1]] + (n/2)*(xi - w[e[0]][e[1]])
        epocas += 1
    print(epocas)        

kohonen()