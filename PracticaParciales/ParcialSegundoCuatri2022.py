#programando pred SubeBaja(s:seq<Z>)
from typing import List
from queue import Queue as Cola

def subeBaja(lista: List[int]) -> bool:
    resultado = False
    pilita = Cola()
    for elem in lista:
        pilita.put(elem)
        #print(elem)
    elementoAnterior = pilita.get()
    elementoActual = pilita.get()
    #print(elementoActual, elementoAnterior)
    if(elementoAnterior > elementoActual):
        resultado = False
    while(elementoAnterior < elementoActual):
        #print(resultado)
        if elementoActual == elementoAnterior:
            resultado = False
            break
        elementoAnterior = elementoActual
        elementoActual = pilita.get()
        #print(elementoActual, elementoAnterior)
        
        if pilita.empty():
            resultado = False
            break
    #print(elementoActual, elementoAnterior)
    
    while(elementoAnterior > elementoActual):
        #print(elementoActual, elementoAnterior)
        
        if elementoActual == elementoAnterior:
            resultado = False
            break
        if pilita.empty():
            resultado = True
            break
        #else:
            #print("te comiste algo")
        elementoAnterior = elementoActual
        elementoActual = pilita.get()
    return resultado

if __name__ == "__main__":
    secuencia = [1,2,3,5,1]
    secuencia2 = [1,7,3,5,1]
    secuencia3 = [-2,-1,3,4,3,2,1]
    
    print("Es subeBaja: ", secuencia, subeBaja(secuencia)) 
    print("Es subeBaja: ", secuencia2, subeBaja(secuencia2)) 
    print("Es subeBaja: ", secuencia3, subeBaja(secuencia3)) 
    
    