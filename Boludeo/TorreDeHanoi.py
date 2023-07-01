def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Mueve n-1 discos de la fuente al auxiliar usando el objetivo como auxiliar
        hanoi(n - 1, source, auxiliary, target)

        # Mueve el disco n de la fuente al objetivo
        target.append(source.pop())

        # Imprime el estado de las torres después del movimiento
        print([source, auxiliary, target])

        # Mueve n-1 discos del auxiliar al objetivo usando la fuente como auxiliar
        hanoi(n - 1, auxiliary, target, source)

# Obtén la cantidad de piezas del usuario
cantidad_piezas = int(input("Ingresa la cantidad de piezas: "))

# Crea la torre inicial
torre_inicial = list(range(1, cantidad_piezas + 1))

# Define las torres
torres = [torre_inicial, [], []]

# Llama a la función hanoi para resolver el problema
hanoi(cantidad_piezas, torres[0], torres[2], torres[1])
