#COLAS (͡ ° ͜ʖ ͡ °)
from typing import List
import Guia10Pilas as funcionesPilas #esto es para poder acceder al otro archivo, no nos van a tomar esto
from queue import Queue as Cola
import Listas

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
def cantidadDeElementos(c : Cola(int)) -> int:
    contador = 0
    while(c.empty() == False):
        contador += 1
        c.get()
    return contador
    
#15
def buscarElMaximo(c : Cola(int)) -> int:
    maximoActual = 0
    while(c.empty() == False):
        numeroEnPila = c.get()
        if(maximoActual < numeroEnPila):
            maximoActual = numeroEnPila
    return maximoActual
    
#16

def armarSecuenciaDeBingo() -> Cola: #no se entiende muy bien la consigna, puede que esté mal
    c = Cola()
    listaBingo = funcionesPilas.generarNrosAlAzar(n=100,desde=0,hasta=99)
    print(listaBingo)
    for numero in listaBingo:
        c.put(numero)
    return c
    
def jugarCartonDeBingo(carton : List[int], bolillero : Cola(int)) -> int:
    cantidadEnCarton = len(carton)
    contador = 0
    while(bolillero.empty() == False):
        numeroActual = bolillero.get()
        contador += 1
        if numeroActual in carton:
            cantidadEnCarton -= 1
        if cantidadEnCarton == 0:
            break
    return contador

#17
def generadorColaPaciente(lista : List) -> Cola((int, str, str)): #bueno por alguna razon esto da error si lo declaras con List[(int, str, str)]
    c = Cola()
    for tupla in lista:
        c.put(tupla)
    return c
def nPacientesUrgentes(c : Cola((int, str, str))) -> int:
    contador = 0
    tuplaActual = (0,"","")
    while(c.empty()==False):
        tuplaActual =  c.get()
        if tuplaActual[0] <= 3:
            contador += 1
    return contador
    
if __name__ == "__main__":
    listaRandom = funcionesPilas.generarNrosAlAzar(n=(11+7),desde=0,hasta=100) #bueno lo del 11 + 7 no tiene mucho sentido, es para darle mas funcionalidad al 14
    print("COLAS (ง ͠° ͟ʖ ͡°)ง\n   Ejercicio 13:   \n      la lista es: ", listaRandom)
    colaDeEnterosMuestra(lista=listaRandom)
    colaEj14 = colaDeEnteros(lista=listaRandom)
    colaEj15 = colaDeEnteros(lista=listaRandom)
    
    print("     Ejercicio 14: ", cantidadDeElementos(colaEj14))
    print("     Ejercicio 15: ", buscarElMaximo(colaEj15))
    cartonchito = funcionesPilas.generarNrosAlAzar(n = 12, desde = 0, hasta = 99)
    secuen = armarSecuenciaDeBingo()
    print("     Ejercicio 16: el carton fue:",cartonchito,"y la cantidad de jugadas: ", jugarCartonDeBingo(carton=cartonchito, bolillero=secuen))
    
    colaMedica1 = generadorColaPaciente(lista=Listas.listaMedica1)
    colaMedica2 = generadorColaPaciente(lista=Listas.listaMedica2)
    colaMedica3 = generadorColaPaciente(lista=Listas.listaMedica3)
    print("     Ejercicio 17: ejemplo 1: ", nPacientesUrgentes(c=colaMedica1))
    print("                   ejemplo 2: ", nPacientesUrgentes(c=colaMedica2))
    print("                   ejemplo 3: ", nPacientesUrgentes(c=colaMedica3))
    
    
    
    