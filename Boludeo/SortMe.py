
#hola mundo
def convertir_caracteres_a_numeros(caracteres):
    correspondencia = {
        " ": 0,
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "ñ": 15,
        "o": 16,
        "p": 17,
        "q": 18,
        "r": 19,
        "s": 20,
        "t": 21,
        "u": 22,
        "v": 23,
        "w": 24,
        "x": 25,
        "y": 26,
        "z": 27
    }
    
    numeros = []
    for caracter in caracteres:
        if caracter in correspondencia:
            numeros.append(correspondencia[caracter])
        else:
            numeros.append(-1)  # Valor de reemplazo para caracteres sin correspondencia
    
    return numeros

# Ejemplo de uso
caracteres = []
texto = 'hola mundo'
for letra in texto:
    caracteres.append(letra)
array = convertir_caracteres_a_numeros(caracteres)
array1 = convertir_caracteres_a_numeros(caracteres)

print(array1)