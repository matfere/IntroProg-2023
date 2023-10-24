# Importar las bibliotecas necesarias
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Datos de entrenamiento: características de los equipos y etiquetas
caracteristicas = np.array([[1, 0], [2, 1], [1, 0], [4, 3], [4, 2], [4, 1], [4, 2], [4, 5]])
etiquetas = np.array([1, 1, 1, 1, 1, 1, 1, 0])

# Crear un modelo de regresión logística
modelo = LogisticRegression()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(caracteristicas, etiquetas, test_size=0.2, random_state=42)

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_entrenamiento, y_entrenamiento)

# Realizar predicciones en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular la precisión del modelo
precision = accuracy_score(y_prueba, predicciones)

# Datos del partido a predecir (características de los equipos)
partido_a_predecir = np.array([[2, 2]])  # Por ejemplo, ambos equipos han anotado 2 goles y encajado 2 goles en partidos anteriores

# Realizar la predicción
prediccion = modelo.predict(partido_a_predecir)

# Imprimir la predicción
if prediccion == 1:
    print("El modelo predice que el equipo local ganará.")
else:
    print("El modelo predice que el equipo visitante ganará.")

# Imprimir la precisión del modelo
print(f"Precisión del modelo en el conjunto de prueba: {precision * 100:.2f}%")
