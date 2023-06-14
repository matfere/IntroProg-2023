import random
from typing import List
from queue import LifoQueue as Pila

#8
def generarNrosAlAzar(n: int, desde: int, hasta: int) -> List[int]:
    numeros = random.sample(range(desde, hasta+1), n)
    return numeros

#9
def pilaAlAzar(lista: List[int]):
    p = Pila()
    for elemento in lista:
        p.put(elemento)
        print("        contiene ", elemento)
    
    return p

#10
def cantidadElementos(p:Pila) -> int:
    contador = 0
    while(p.empty() == False):
        p.get()
        contador += 1
    
    return contador

#11
def buscarElMaximo(p:Pila) -> int:
    maximoActual = 0
    while(p.empty() == False):
        numeroEnPila = p.get()
        if(maximoActual < numeroEnPila):
            maximoActual = numeroEnPila
    return maximoActual

#12
def cantidadParentesis1(p:Pila) -> int:
    contador = 0
    elemento = ""
    while(p.empty() == False):
        elemento = p.get()
        if elemento == "(":
            contador += 1
    return contador

def cantidadParentesis2 (p:Pila) -> int:
    contador = 0
    while(p.empty() == False):
        elemento = p.get()
        if elemento == ")":
            contador += 1
    return contador

def estaBienBalanceada(s: str) -> bool: #aca lo unico que realmente importa son los parentesis, si la cantidad entre los "(" corresponde con la cantidad de ")" entonces es valido
    p1 = Pila()
    p2 = Pila()
    for letras in s:
        p1.put(letras)
        p2.put(letras)
    if cantidadParentesis1(p=p1) == cantidadParentesis2(p=p2):
        return True
    else:
        return False
    
if __name__ == "__main__": # para no pasarme poniendo numeritos puse los valores de una, si queres ingresarlos vos podes reemplazar los numeros por int(input('texto a devolver'))
    
    malBalanceada = "( 1 + 2 ( 32 + 27 ) + 32 ) )"
    bienBalanceada = "1 + ( 2 x 3 − ( 20 / 5 ) )"
    
    listaAzar = generarNrosAlAzar(n = 10, desde = 0, hasta = 10)
    print("Pilas \n    Ejercicio 8:    ", listaAzar)
    print("    Ejercicio 9:    ")
    pilita = pilaAlAzar(lista=listaAzar)
    pilita2 = pilaAlAzar(lista=listaAzar)
    print("    Ejercicio 10:    ", cantidadElementos(p = pilita))
    print("    Ejercicio 11:    ", buscarElMaximo(p = pilita2)) #tener en cuenta que cada vez que se usa get se elimina el ultimo elemento, por lo que las pilas quedan vacias despues de utilizarlas
    print("    Ejercicio 12:    ",malBalanceada + " : ", estaBienBalanceada(s = malBalanceada))
    print("                     ",bienBalanceada + " : ", estaBienBalanceada(s = bienBalanceada)) #esta medio mal esto, si pones algo con esta pinta: )()(, te va a decir que esta bien, me da paja corregirlo
    
    