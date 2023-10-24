from typing import List
# Función para verificar si un número contiene al menos un 7
def contiene_siete(numero):
    return '7' in str(numero)

# Generar todas las listas de cuatro cifras que contienen al 7
listas_con_siete = [num for num in range(10000) if contiene_siete(num)]

# Imprimir las listas
for lista in listas_con_siete:
    print("{:04}".format(lista))
print(len(listas_con_siete))