"""
Taller de Laboratorio Final: Programando un Kernel
Sesion 1 - Refuerzo Python y Algebra Lineal - Inteligencia Artificial II

Simulador basico de convolucion 3x3 (sin OpenCV): producto Hadamard entre
la seccion de imagen y el kernel, sumando todos los valores resultantes.
"""
import numpy as np

I = np.array([[100, 100, 100],
              [100, 200, 100],
              [100, 100, 100]])

K = np.array([[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]])

pixel_central = np.sum(I * K)  # Hadamard + suma total
print("Valor del pixel central calculado:", pixel_central)
