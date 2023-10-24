from typing import List
import time

def EsPrimoClasic(lista: List[int]) -> List[int]:
    listaPrimos = [2]
    for i in range(0, len(lista)):
        for j in range(2, lista[i]):
            if(lista[i] % j == 0):
                break
            if (lista[i] % j != 0 and j == (lista[i] - 1)):
                listaPrimos.append(lista[i])
    return listaPrimos

def euclides_mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def esCoprimo (a,b):
    if (euclides_mcd(a=a,b=b) == 1):
        return True
    return False


def EsPrimoCoprimo(lista: List[int]) -> List[int]:
    listaPrimos = [2]
    for i in range(0, len(lista)):
        if(lista[i] % 2 != 0):
            mitad = (lista[i]+1)/2
            while(esCoprimo(lista[i], mitad)):
                if(mitad != lista[i]):
                    mitad += 1
                    #print(mitad, lista[i])
                if(mitad == lista[i]):
                    if(lista[i] != 1):
                        listaPrimos.append(lista[i])
                    break
                

    return listaPrimos

if __name__ == "__main__":
    inicio = time.time()
    listaEnteros = []
    for i in range(1,10001):
        listaEnteros.append(i)
    print("Se analizaron: ",len(listaEnteros))
    print("los primos son: ", len(EsPrimoClasic(lista=listaEnteros)))
    #print("es coprimo 6 8: ", esCoprimo(6,8))
    print("los primos aprox son: ", len(EsPrimoCoprimo(lista=listaEnteros)))
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_transcurrido} segundos")
    