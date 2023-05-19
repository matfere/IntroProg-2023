import math
    
#ej1

#1
def raizDe2() -> float:
    numero = math.sqrt(2)
    return round(numero, 4)

#2
def imprimir_hola() -> str:
    return "hola"

#3
def imprimir_un_verso() -> str:
    return "Que casualidad fue encontarte justo aca, yo tan puesto vos tan apuesta"

#4
def factorial_2() -> int:
    a = 1
    hasta = 2
    hasta = hasta + 1
    for i in range(1,hasta, 1): #recordar que range(desde, hasta, con paso)
        a = a * i
    return a

#5
def factorial_3() -> int:
    a = 1
    hasta = 3
    hasta = hasta + 1
    for i in range(1,hasta, 1):
        a = a * i
    return a

#6
def factorial_4() -> int:
    a = 1
    hasta = 4
    hasta = hasta + 1
    for i in range(1,hasta, 1):
        a = a * i
    return a

#7
def factorial_5() -> int:
    a = 1
    hasta = 5
    hasta = hasta + 1
    for i in range(1,hasta, 1):
        a = a * i
    return a


#Ejercicio 2

#1
def imprimir_saludo(nombre: str) -> str:
    resultado = "Hola " + nombre
    return resultado

#2
def raiz_cuadrada_de(numero: float) -> float:
    return math.sqrt(numero)

#3
def imprimir_dos_veces(estribillo: str) -> str:
    return (estribillo + "\n" + estribillo)

print("Ejercicio 1 \n")
print("1) ", raizDe2())
print("2) ", imprimir_hola())
print("3) ", imprimir_un_verso())
print("4) ", factorial_2())
print("5) ", factorial_3())
print("6) ", factorial_4())
print("7) ", factorial_5(), "\n")

print("Ejercicio 2 \n")
print("1)", imprimir_saludo(nombre = str(input("ingresa tu nombre: \n"))))
print("2)", raiz_cuadrada_de(numero = float(input("ingresa un numero: \n"))))
print("3)\n", imprimir_dos_veces(estribillo = str(input("ingresa tu estribillo: \n"))))






