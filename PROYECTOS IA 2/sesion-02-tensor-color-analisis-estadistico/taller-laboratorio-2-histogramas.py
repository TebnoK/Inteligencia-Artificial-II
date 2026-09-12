"""
Taller de Laboratorio 2: Analisis estadistico por canal
Sesion 2 - Tensor de color y analisis estadistico - Inteligencia Artificial II

Calcula y grafica los histogramas B, G y R superpuestos. Puede recibir una
ruta de imagen como primer argumento; sin ruta usa una imagen de prueba.
"""
import sys

import matplotlib.pyplot as plt
import numpy as np


def crear_imagen_prueba():
    """Crea una imagen BGR con zonas de color para observar los histogramas."""
    imagen = np.zeros((120, 180, 3), dtype=np.uint8)
    imagen[:, :60] = [255, 40, 20]
    imagen[:, 60:120] = [30, 190, 40]
    imagen[:, 120:] = [20, 40, 220]
    return imagen


def cargar_imagen(ruta):
    """Carga una imagen BGR con OpenCV si el usuario proporciona una ruta."""
    import cv2

    imagen = cv2.imread(ruta)
    if imagen is None:
        raise SystemExit(f"No se pudo leer la imagen: {ruta}")
    return imagen


def main():
    imagen = cargar_imagen(sys.argv[1]) if len(sys.argv) > 1 else crear_imagen_prueba()
    nombres = ("Azul", "Verde", "Rojo")
    colores = ("blue", "green", "red")

    plt.figure(figsize=(10, 5))
    for indice, (nombre, color) in enumerate(zip(nombres, colores)):
        histograma, _ = np.histogram(imagen[:, :, indice], bins=256, range=(0, 256))
        plt.plot(histograma, color=color, label=f"Canal {nombre}")
        print(f"Canal {nombre}: intensidad mas frecuente = {histograma.argmax()}")

    plt.title("Distribucion de intensidades por canal BGR")
    plt.xlabel("Valor del pixel (0-255)")
    plt.ylabel("Frecuencia (cantidad de pixeles)")
    plt.xlim(0, 255)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
