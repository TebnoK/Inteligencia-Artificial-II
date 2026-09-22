"""
Taller de laboratorio: explorando las matrices
Sesión 12 - Redes neuronales densas o multicapa
"""

import numpy as np


def sigmoide(z):
    return 1 / (1 + np.exp(-z))


def propagacion_hacia_adelante(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoide(Z1)
    Z2 = np.dot(A1, W2) + b2
    salida = sigmoide(Z2)
    return Z1, A1, Z2, salida


def main():
    X = np.array([0.5, 0.8, 0.2])

    W1 = np.array([
        [0.1, 0.2, 0.3, 0.4],
        [-0.5, 0.6, 0.7, -0.8],
        [0.9, -0.1, 0.2, 0.3],
    ])
    b1 = np.array([0.1, -0.2, 0.3, -0.4])

    W2 = np.array([[0.5], [-0.6], [0.7], [0.8]])
    b2 = np.array([-0.1])

    Z1, A1, Z2, salida = propagacion_hacia_adelante(X, W1, b1, W2, b2)

    print("Cliente 1")
    print("Z1:", np.round(Z1, 4))
    print("A1:", np.round(A1, 4))
    print("Z2:", np.round(Z2, 4))
    print("Salida:", np.round(salida, 4))

    X_dos_clientes = np.array([
        [0.5, 0.8, 0.2],
        [0.1, 0.9, 0.9],
    ])

    Z1_lote, A1_lote, Z2_lote, salida_lote = propagacion_hacia_adelante(
        X_dos_clientes, W1, b1, W2, b2
    )

    print("\nDos clientes")
    print("Salidas:")
    print(np.round(salida_lote, 4))


if __name__ == "__main__":
    main()
