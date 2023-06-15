from typing import List
import Guia10Archivos as Archivos
import csv
#DICCIONARIOS

#Ejercicio 18
def agruparPorLongitud(nombre_archivo : str) -> dict: #siento que estuvo medio falopa lo que hice, seguramente haya una forma mas sencilla de lograr lo mismo
    archivo = open(nombre_archivo, 'r', encoding="utf-8")
    texto = archivo.read()
    archivo.close()
    listaPalabras = texto.split()
    cantidadDeLetrasEnPalabra = []
    diccionario = {}
    palabraMasLarga = 0
    for palabra in listaPalabras: #convierto todo el archivo en una lista de numeros
        if palabraMasLarga < len(palabra): #encuentro el numero mas grande
            palabraMasLarga = len(palabra)
        cantidadDeLetrasEnPalabra.append(len(palabra))
    for numero in range(0, palabraMasLarga + 1): #cuento la cantidad de veces que aparece cada numero, si hay un numero en el rango que no aparece quiero que no lo muestre
        if numero in cantidadDeLetrasEnPalabra:
            diccionario[numero] = cantidadDeLetrasEnPalabra.count(numero)
    return diccionario

#19
def promedioAlumnos() -> dict:
    promediosPorAlumno = {}
    listaDeLU = []
    with open("C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/alumnos.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)  #saltar la primera línea que contiene los encabezados
        for alumnos in reader:
            if alumnos[0] not in listaDeLU:
                listaDeLU.append(alumnos[0])
        for LU in listaDeLU:
            promediosPorAlumno[LU] = Archivos.promedioEstudiante(lu=LU)
    return promediosPorAlumno

if __name__ == "__main__":
    nombreDelArchivo = "C:/Users/matu/Desktop/Facultad/Repos/IntroProg/IntroProg-2023/Guias/puesto.txt"
    print("Diccionarios\n   Ejercicio 18: ", agruparPorLongitud(nombre_archivo=nombreDelArchivo))
    print("   Ejercicio19: ", promedioAlumnos())