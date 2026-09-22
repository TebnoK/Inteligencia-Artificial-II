"""
Taller de laboratorio: hackeando los pesos
Sesión 11 - Redes neuronales: el perceptrón
"""

import numpy as np


def funcion_escalon(z):
    if z >= 0:
        return 1
    return 0


def perceptron(X, w, b):
    z = np.dot(X, w) + b
    salida = funcion_escalon(z)
    return salida


def main():
    # Código base: compuerta AND
    entradas_and = np.array([1, 1])
    pesos_and = np.array([0.5, 0.5])
    sesgo_and = -0.8

    resultado_and = perceptron(entradas_and, pesos_and, sesgo_and)
    print("Resultado AND para [1, 1]:", resultado_and)

    # Pesos modificados manualmente para resolver la compuerta OR
    entradas_or = np.array([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ])
    pesos_or = np.array([0.5, 0.5])
    sesgo_or = -0.4

    print("\nResultados OR:")
    for entrada in entradas_or:
        resultado = perceptron(entrada, pesos_or, sesgo_or)
        print(f"{entrada.tolist()} -> {resultado}")

    print("\nPesos OR:", pesos_or)
    print("Sesgo OR:", sesgo_or)
    print("\nUna neurona real no ajusta estos pesos por sí sola: necesita un proceso de entrenamiento.")


if __name__ == "__main__":
    main()
