#COLAS (͡ ° ͜ʖ ͡ °)
from typing import List
import Guia10Pilas as funcionesPilas #esto es para poder acceder al otro archivo, no nos van a tomar esto
from queue import Queue as Cola

#13
def colaDeEnterosMuestra(lista: List[int]): #esto es para mostrar como funca, lo que pide el ejercicio está mas abajo
    c = Cola()
    for numero in lista:
        c.put(numero)
        print("         Entro: ", numero)
    for elemento in lista:
        print("         salio: ", c.get())
        
        
def colaDeEnteros(lista: List[int]) -> Cola:
    c = Cola()
    for numero in lista:
        c.put(numero)
    return c
        
#14
def cantidadDeElementos(c : Cola) -> int:
    contador = 0
    while(c.empty() == False):
        contador += 1
        c.get()
    return contador
    
#15
def buscarElMaximo(c : Cola) -> int:
    maximoActual = 0
    while(c.empty() == False):
        numeroEnPila = c.get()
        if(maximoActual < numeroEnPila):
            maximoActual = numeroEnPila
    return maximoActual
    
#16

    
if __name__ == "__main__":
    listaRandom = funcionesPilas.generarNrosAlAzar(n=(11+7),desde=0,hasta=100) #bueno lo del 11 + 7 no tiene mucho sentido, es para darle mas funcionalidad al 14
    print("COLAS (ง ͠° ͟ʖ ͡°)ง\n   Ejercicio 13:   \n      la lista es: ", listaRandom)
    colaDeEnterosMuestra(lista=listaRandom)
    colaEj14 = colaDeEnteros(lista=listaRandom)
    colaEj15 = colaDeEnteros(lista=listaRandom)
    
    print("     Ejercicio 14: ", cantidadDeElementos(colaEj14))
    print("     Ejercicio 15: ", buscarElMaximo(colaEj15))
    