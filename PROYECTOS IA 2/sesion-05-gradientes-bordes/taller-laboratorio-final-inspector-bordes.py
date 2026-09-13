"""
Taller de Laboratorio: Inspector de bordes
Sesion 5 - Gradientes espaciales y deteccion de bordes - Inteligencia Artificial II

Calcula bordes verticales con Sobel X, horizontales con Sobel Y y bordes
combinados con Canny. Guarda un panel comparativo y varias configuraciones
para experimentar con los umbrales de Canny.
"""
import sys
from pathlib import Path

import cv2
import numpy as np


CARPETA_SESION = Path(__file__).resolve().parent
RUTA_IMAGEN_PREDETERMINADA = CARPETA_SESION / "imagenes" / "imagen-bordes.jpg"
CONFIGURACIONES_CANNY = ((10, 50), (50, 150), (200, 250))


def cargar_imagen(ruta):
    imagen = cv2.imread(str(ruta), cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise SystemExit(
            "No se pudo leer la imagen. Coloca una imagen en "
            f"'{RUTA_IMAGEN_PREDETERMINADA}' o indica su ruta como primer argumento."
        )
    return imagen


def normalizar_gradiente(gradiente):
    """Convierte valores negativos y positivos a una imagen visible de 8 bits."""
    return cv2.convertScaleAbs(gradiente)


def crear_panel(imagen, sobel_x, sobel_y, bordes_canny):
    """Organiza las cuatro vistas en una sola imagen comparativa."""
    imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
    sobel_x_color = cv2.cvtColor(sobel_x, cv2.COLOR_GRAY2BGR)
    sobel_y_color = cv2.cvtColor(sobel_y, cv2.COLOR_GRAY2BGR)
    canny_color = cv2.cvtColor(bordes_canny, cv2.COLOR_GRAY2BGR)
    fila_superior = np.hstack((imagen_color, sobel_x_color))
    fila_inferior = np.hstack((sobel_y_color, canny_color))
    return np.vstack((fila_superior, fila_inferior))


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else RUTA_IMAGEN_PREDETERMINADA
    carpeta_salida = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else CARPETA_SESION / "resultados-sesion-05"
    )
    imagen = cargar_imagen(ruta)

    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    sobel_x_visible = normalizar_gradiente(sobel_x)
    sobel_y_visible = normalizar_gradiente(sobel_y)

    carpeta_salida.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(carpeta_salida / "sobel-x-verticales.png"), sobel_x_visible)
    cv2.imwrite(str(carpeta_salida / "sobel-y-horizontales.png"), sobel_y_visible)

    for umbral_bajo, umbral_alto in CONFIGURACIONES_CANNY:
        bordes_canny = cv2.Canny(imagen, umbral_bajo, umbral_alto)
        nombre = f"canny-{umbral_bajo}-{umbral_alto}.png"
        cv2.imwrite(str(carpeta_salida / nombre), bordes_canny)

    bordes_canny = cv2.Canny(imagen, 50, 150)
    panel = crear_panel(imagen, sobel_x_visible, sobel_y_visible, bordes_canny)
    cv2.imwrite(str(carpeta_salida / "panel-comparativo.png"), panel)

    print(f"Imagen procesada: {ruta}")
    print("Sobel X: bordes verticales")
    print("Sobel Y: bordes horizontales")
    print(f"Configuraciones Canny: {CONFIGURACIONES_CANNY}")
    print(f"Resultados guardados en: {carpeta_salida}")


if __name__ == "__main__":
    main()
