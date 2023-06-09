from typing import List

archivo = open("Puesto.txt")

#EJ1
#   1.1
def contarLineas(archivo: List[str]) -> int:
    contador = 0
    for linea in archivo:
        contador += 1
    return contador

#   1.2

if __name__ == "__main__":
    print("EJ1 \n","    1.1 contando lineas: \n","       ", contarLineas(archivo.readlines()))