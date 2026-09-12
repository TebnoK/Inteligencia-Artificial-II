"""
Taller de Laboratorio Final: Estrategias de suavizado
Sesion 4 - Convolucion - Inteligencia Artificial II

Compara filtro de media, Gaussiano y mediana con kernel 7x7 sobre una imagen
con ruido de sal y pimienta. Sin ruta usa una imagen sintetica reproducible.
Los resultados se guardan en una carpeta para compararlos visualmente.
"""
import sys
from pathlib import Path

import cv2
import numpy as np


KERNEL_SIZE = 7


def crear_imagen_con_ruido():
    """Genera un objeto con textura y ruido impulsivo blanco/negro."""
    rng = np.random.default_rng(42)
    imagen = np.full((240, 360), 55, dtype=np.uint8)
    cv2.rectangle(imagen, (95, 55), (265, 185), 175, -1)
    cv2.circle(imagen, (180, 120), 42, 205, -1)

    cantidad_ruido = 1400
    filas = rng.integers(0, imagen.shape[0], cantidad_ruido)
    columnas = rng.integers(0, imagen.shape[1], cantidad_ruido)
    valores = rng.choice((0, 255), cantidad_ruido)
    imagen[filas, columnas] = valores
    return imagen


def cargar_imagen(ruta):
    imagen = cv2.imread(str(ruta), cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise SystemExit(f"No se pudo leer la imagen: {ruta}")
    return imagen


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    carpeta_salida = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else Path(__file__).resolve().parent / "resultados-sesion-04"
    )
    imagen = cargar_imagen(ruta) if ruta else crear_imagen_con_ruido()

    kernel_media = (KERNEL_SIZE, KERNEL_SIZE)
    imagen_media = cv2.blur(imagen, kernel_media)
    imagen_gaussiana = cv2.GaussianBlur(imagen, kernel_media, 0)
    imagen_mediana = cv2.medianBlur(imagen, KERNEL_SIZE)

    carpeta_salida.mkdir(parents=True, exist_ok=True)
    resultados = {
        "original-con-ruido.png": imagen,
        "filtro-media-7x7.png": imagen_media,
        "filtro-gaussiano-7x7.png": imagen_gaussiana,
        "filtro-mediana-7x7.png": imagen_mediana,
    }
    for nombre, resultado in resultados.items():
        cv2.imwrite(str(carpeta_salida / nombre), resultado)

    print(f"Kernel media y Gaussiano: {KERNEL_SIZE}x{KERNEL_SIZE}")
    print(f"Kernel mediana: {KERNEL_SIZE}")
    print(f"Resultados guardados en: {carpeta_salida}")
    print("La media difumina y puede crear tonos grises alrededor del ruido.")
    print("La mediana descarta mejor los extremos y conserva los bordes.")


if __name__ == "__main__":
    main()
