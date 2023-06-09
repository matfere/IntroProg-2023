from typing import List


#EJ1
#   1.1
def contarLineas(archivo: List[str]) -> int:
    contador = 0
    for linea in archivo:
        contador += 1
    return contador

#   1.2
def existePalabra(palabra: str, archivo: List[str]) -> bool:
    for linea in archivo:
        if palabra.lower() in linea.lower():
            return True
    return False

#   1.3
def cantidadDeApariciones(archivo: List[str], palabra: str) -> int:
    contador = 0
    for linea in archivo:
        if palabra.lower() in linea.lower():
            contador += 1
    return contador

#EJ2


if __name__ == "__main__":
    archivo0 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puesto.txt", 'r')
    archivo1 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puesto.txt", 'r') #notar que cada ejercicio necesita un archivo distinto
    archivo2 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puesto.txt", 'r')
    
    
    codigoParaEl2 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/Guia7.py", 'r')
    

    print("EJ1 \n","    1.1 contando lineas: \n","       ", contarLineas(archivo0.readlines()))
    print("    1.2 existe palabra: \n","       ", existePalabra(palabra = str(input("ingresar palabra ")), archivo = archivo1.readlines()))
    print("    1.3 cantidad de apariciones: \n","       ", cantidadDeApariciones(archivo = archivo2.readlines(), palabra = str(input("ingresar palabra "))))
    
    