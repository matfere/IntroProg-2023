from typing import List

#Manejo de archivos // esto no lo toman pero esta bueno saberlo igual

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
def clonarSinComentarios(archivo: str) -> str:
    lineas = archivo.splitlines()
    texto = ""
    for linea in lineas:
        
        if linea.strip() and linea.strip()[0] !="#": # la función strip() se utiliza para eliminar los espacios en blanco antes y después de cada línea
            texto += linea + "\n"
        else:               #esto no lo pide la consigna pero asi queda mas lindo
            texto += "\n"
        
    return texto

#EJ3 aclaracion, hice otra cosa, de apurado flashee que el ejercicio pedia dar vuelta cada letra manteniendo el orden, me parecio util igual asi que lo dejo :D

def darVuelta(texto: str) -> str:
    salida = ""
    
    for letra in range(len(texto) - 1, -1, -1):
        salida += texto[letra]
    
    return salida


def archivoAlveres(archivoOrigen: str) -> str:
    lineas = archivoOrigen.splitlines()
    texto = ""

    for linea in lineas:
        linea_al_reves = darVuelta(linea)
        texto += linea_al_reves + "\n"
    
    return texto





if __name__ == "__main__":
    
    rutaPuesto = "C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puesto.txt"
    
    archivo0 = open(rutaPuesto, "r", encoding='utf8')
    archivo1 = open(rutaPuesto, "r", encoding='utf8') #notar que cada ejercicio necesita un archivo distinto
    archivo2 = open(rutaPuesto, "r", encoding='utf8')
    
    
    codigoParaEl2 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/Guia7.py", 'r')
    
    archivo3 = open(rutaPuesto, "r", encoding='utf8')
    dameVuelta3 = open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puestont.txt", "w", encoding='utf8')
    
    
    #EJ1
    print("EJ1 \n","    1.1 contando lineas: \n","       ", contarLineas(archivo0.readlines()))
    print("    1.2 existe palabra: \n","       ", existePalabra(palabra = str(input("ingresar palabra ")), archivo = archivo1.readlines()))
    print("    1.3 cantidad de apariciones: \n","       ", cantidadDeApariciones(archivo = archivo2.readlines(), palabra = str(input("ingresar palabra "))))
    
    #EJ2
    print("EJ2 \n","    Clonar sin comentarios: \n", clonarSinComentarios(codigoParaEl2.read()))
    
    #EJ3
    contenido = archivo3.read()
    archivo3.close()

    resultado = archivoAlveres(contenido)
    print(resultado)
    dameVuelta3.write(resultado)
    