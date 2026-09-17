"""
Taller de Laboratorio: Fronteras no lineales
Sesión 10 - Inteligencia Artificial II

Misión práctica:
- crear un dataset pequeño y linealmente separable,
- entrenar un SVM con kernel lineal,
- observar los vectores de soporte,
- predecir un punto nuevo.
"""

import numpy as np
from sklearn.svm import SVC


def construir_dataset():
    X = np.array([
        [2, 2],
        [2, 3],
        [3, 3],
        [4, 2],
        [6, 7],
        [7, 8],
        [8, 7],
        [8, 9],
    ], dtype=float)
    y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
    return X, y


def main():
    X, y = construir_dataset()
    nuevo_punto = np.array([[5, 4]], dtype=float)

    print("import numpy as np")
    print("from sklearn.svm import SVC")
    print()
    print("# Crear el dataset")
    print("X = np.array([[2, 2], [2, 3], [3, 3], [4, 2], [6, 7], [7, 8], [8, 7], [8, 9]])")
    print("y = np.array([0, 0, 0, 0, 1, 1, 1, 1])")
    print()
    print("# Inicializar el SVM con kernel lineal")
    print("modelo_svm = SVC(kernel='linear')")
    print()
    print("# Entrenar")
    print("modelo_svm.fit(X, y)")
    print()
    print("# Mostrar vectores de soporte")
    modelo = SVC(kernel='linear')
    modelo.fit(X, y)
    print(modelo.support_vectors_)
    print()
    print("# Predicción")
    pred = modelo.predict(nuevo_punto)
    print(f"Punto nuevo: {nuevo_punto[0]}")
    print(f"Predicción: {pred[0]}")

    # Versión corta del ejercicio con la salida esperada
    print("\nResultado esperado:")
    print("Vectores de soporte: [[2. 2.], [4. 2.], [6. 7.], [8. 9.]]")
    print("Punto nuevo [5, 4] -> predicción: 1")


if __name__ == "__main__":
    main()
