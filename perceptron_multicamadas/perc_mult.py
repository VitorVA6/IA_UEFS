import numpy as np 

def read_file():
    file = open('dataset/iris-10-1tra.dat', 'r')
    dados = file.read().split('\n')[9:]
    dados = [item.split(', ') for item in dados]
    x = [list(map(float, item[0:4])) for item in dados]
    d = [item[4] for item in dados]
    return x, d

x, d = read_file()