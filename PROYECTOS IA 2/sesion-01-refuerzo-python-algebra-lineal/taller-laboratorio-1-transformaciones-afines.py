"""
Taller de Laboratorio 1: Transformaciones Afines
Sesion 1 - Refuerzo Python y Algebra Lineal - Inteligencia Artificial II

Reto: reducir el contraste 50% y el brillo en 50 unidades de una imagen
sobreexpuesta (radiografia), acotando el resultado a 8 bits.
"""
import numpy as np

np.random.seed(42)
original = np.random.randint(200, 255, (5, 5))

alpha, beta = 0.5, -50  # 50% menos contraste, -50 de brillo
procesada = np.clip(alpha * original + beta, 0, 255).astype(np.uint8)

print("Matriz original:\n", original)
print("\nMatriz procesada (contraste 50%, brillo -50):\n", procesada)
