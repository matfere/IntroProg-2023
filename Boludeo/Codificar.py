import SortingQuickSort
import SortMe
archivoCodificar = open("codificado.txt", 'w', encoding='utf-8')
arreglo = SortMe.array1 #hola mundo
arreglo1 = SortMe.array
codificando = SortingQuickSort.quickSort(arreglo=arreglo, min=0, max=len(arreglo)-1)
print(arreglo1)
print(codificando)
codificado = SortingQuickSort.comparar_listas(lista1=arreglo1, lista2=codificando)
#codificado.sort()
print(codificado)
#archivoCodificar.write(str(arreglo1) + '\n')
archivoCodificar.write(str(codificando) + '\n')

archivoCodificar.write(str(codificado) + '\n')
archivoCodificar.close()