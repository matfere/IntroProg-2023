from typing import List
#tene en cuenta que python ya trae una funcion Sort() pero estoy al pedo asi que la voy a hacer yo :)
def particion(arreglo: List[int], min: int, max: int) -> int:
    pivote = arreglo[max]
    i = min - 1
    
    for j in range(min, max):
        if arreglo[j] <= pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    
    arreglo[i+1], arreglo[max] = arreglo[max], arreglo[i+1]
    return i + 1
    
def quickSort(arreglo: List[int], min: int, max: int):
    if min < max:
        pi = particion(arreglo=arreglo, min=min, max=max)
        quickSort(arreglo=arreglo, min=min, max=pi-1)
        quickSort(arreglo=arreglo, min=pi+1, max=max)
    
    return arreglo

def comparar_listas(lista1, lista2): #desorden, orden
    cambios = []
    for i, elemento in enumerate(lista1):
        if elemento != lista2[i]:
            cambios.append([elemento, lista2[i]])
    return cambios

