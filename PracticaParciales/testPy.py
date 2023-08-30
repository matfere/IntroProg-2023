from typing import List

def decodificar(tuplas, secuencia):
    dic = {}
    res = []
    for x,y in tuplas:
        dic[x] = y
    for letra in secuencia:
        res.append(dic[letra])
    return res

tuplas = [('a','b'),('b','c'),('c','d'),('d','e')]
secuencia = ['a', 'd', 'c']
print(decodificar(tuplas=tuplas, secuencia=secuencia))