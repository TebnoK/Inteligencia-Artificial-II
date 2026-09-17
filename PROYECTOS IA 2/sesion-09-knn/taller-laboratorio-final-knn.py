"""
Taller de Laboratorio: Clasificador Universal
Sesión 9 - Inteligencia Artificial II

Misión práctica:
- construir un dataset con 3 características,
- entrenar un clasificador KNN manualmente,
- probar con K=1 y K=5,
- analizar el efecto de la dimensionalidad.
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def construir_dataset():
    """Dataset con 3 características: Edad, salario y número de hijos."""
    X = np.array(
        [
            [20, 30, 0],
            [40, 50, 2],
            [35, 45, 1],
            [25, 25, 0],
            [55, 70, 3],
            [30, 38, 1],
            [60, 85, 4],
            [18, 22, 0],
            [45, 60, 2],
            [33, 40, 1],
            [50, 65, 3],
            [27, 34, 0],
        ],
        dtype=float,
    )

    y = np.array(
        [
            "NO COMPRA",
            "COMPRA",
            "COMPRA",
            "NO COMPRA",
            "COMPRA",
            "NO COMPRA",
            "COMPRA",
            "NO COMPRA",
            "COMPRA",
            "NO COMPRA",
            "COMPRA",
            "NO COMPRA",
        ]
    )

    return X, y


def predecir_k_vecinos(X, y, nuevo_punto, k):
    """Entrena KNN y predice la clase para un punto nuevo."""
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X, y)
    prediccion = modelo.predict([nuevo_punto])[0]
    print(f"\nResultado con K={k}:")
    print(f"Punto nuevo: {nuevo_punto}")
    print(f"Predicción: {prediccion}")
    return prediccion


def mostrar_analisis_dimensionalidad():
    """Explica la maldición de la dimensionalidad en palabras simples."""
    print("\nAnálisis: la maldición de la dimensionalidad")
    print("Si en lugar de 3 columnas tuviéramos 1000 columnas (como los píxeles de una imagen),")
    print("la distancia euclidiana entre dos puntos se volvería mucho menos informativa:")
    print("- los puntos se dispersan en un espacio más grande;")
    print("- la diferencia entre distancias vecinas se vuelve pequeña;")
    print("- los vecinos más cercanos pueden dejar de representar bien la estructura del dato;")
    print("- el algoritmo necesita más datos para cubrir ese espacio de forma útil.")


def main():
    X, y = construir_dataset()
    nuevo_punto = np.array([40, 40, 1], dtype=float)

    print("Dataset de entrenamiento:")
    print(X)
    print("\nEtiquetas:")
    print(y)

    predecir_k_vecinos(X, y, nuevo_punto, 1)
    predecir_k_vecinos(X, y, nuevo_punto, 5)
    mostrar_analisis_dimensionalidad()


if __name__ == "__main__":
    main()
