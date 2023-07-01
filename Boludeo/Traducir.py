def convertir_numeros_a_caracteres(numeros):
    correspondencia = {
        0: " ",
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "j",
        11: "k",
        12: "l",
        13: "m",
        14: "n",
        15: "ñ",
        16: "o",
        17: "p",
        18: "q",
        19: "r",
        20: "s",
        21: "t",
        22: "u",
        23: "v",
        24: "w",
        25: "x",
        26: "y",
        27: "z"
    }
    
    caracteres = []
    for numero in numeros:
        if numero in correspondencia:
            caracteres.append(correspondencia[numero])
        else:
            caracteres.append("?")  # Carácter de reemplazo para números sin correspondencia
    
    return caracteres

# Ejemplo de uso
archivoCodificado = open("codificado.txt", "r", encoding="utf-8")
listaCodificado = archivoCodificado.readlines()
archivoCodificado.close()
numeros = []
for elemento in listaCodificado[0]:
    if elemento.isdigit():
        numeros.append(int(elemento))
print(numeros)

numerosOrden = []
for elemento in listaCodificado[1]:
    if elemento.isdigit():
        numerosOrden.append(int(elemento))
print(numerosOrden)
texto = ""
for letras in convertir_numeros_a_caracteres(numeros=numeros):
    texto += letras
resultado = texto
print(resultado)
