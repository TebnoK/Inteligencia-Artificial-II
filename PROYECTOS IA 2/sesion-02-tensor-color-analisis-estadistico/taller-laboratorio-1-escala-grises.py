"""
Taller de Laboratorio 1: Transformacion de espacios de color
Sesion 2 - Tensor de color y analisis estadistico - Inteligencia Artificial II

Calcula manualmente el gris de un pixel BGR y lo contrasta con OpenCV.
Si no se indica una imagen, se genera una imagen BGR de prueba.
"""
import sys

import cv2
import numpy as np

PESOS_BGR = np.array([0.114, 0.587, 0.299], dtype=np.float64)


def crear_imagen_prueba():
    """Construye una imagen BGR pequena para ejecutar el taller sin archivos externos."""
    return np.array(
        [
            [[0, 255, 255], [255, 0, 0]],
            [[0, 255, 0], [0, 0, 255]],
        ],
        dtype=np.uint8,
    )


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else None
    imagen = cv2.imread(ruta) if ruta else crear_imagen_prueba()

    if imagen is None:
        raise SystemExit(f"No se pudo leer la imagen: {ruta}")

    pixel_amarillo = np.array([0, 255, 255], dtype=np.uint8)
    gris_manual = float(np.dot(pixel_amarillo.astype(np.float64), PESOS_BGR))
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    print("Pixel amarillo BGR:", pixel_amarillo)
    print("Gris manual del pixel amarillo:", gris_manual)
    print("Gris redondeado a 8 bits:", round(gris_manual))
    print("Imagen cargada con shape BGR:", imagen.shape)
    print("Imagen convertida a escala de grises:\n", imagen_gris)


if __name__ == "__main__":
    main()
