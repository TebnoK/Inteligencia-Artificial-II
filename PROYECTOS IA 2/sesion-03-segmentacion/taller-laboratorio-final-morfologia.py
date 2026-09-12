"""
Taller de Laboratorio Final: Limpiando la vision
Sesion 3 - Segmentacion - Inteligencia Artificial II

Aplica umbralizacion, apertura y cierre morfologicos usando un kernel 3x3.
Usa una imagen sintetica si no se proporciona una ruta y guarda los tres
resultados para poder compararlos visualmente.
"""
import sys
from pathlib import Path

import cv2
import numpy as np


def crear_imagen_prueba():
    """Genera un objeto blanco con ruido de sal y pimienta."""
    imagen = np.full((180, 260), 35, dtype=np.uint8)
    cv2.rectangle(imagen, (70, 45), (190, 135), 210, -1)
    imagen[20, 25] = 255
    imagen[150, 230] = 255
    imagen[75, 120] = 0
    imagen[110, 145] = 0
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
        else Path(__file__).resolve().parent / "resultados-sesion-03"
    )
    imagen = cargar_imagen(ruta) if ruta else crear_imagen_prueba()

    _, original_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), dtype=np.uint8)
    imagen_apertura = cv2.morphologyEx(
        original_binaria, cv2.MORPH_OPEN, kernel, iterations=1
    )
    imagen_cierre = cv2.morphologyEx(
        original_binaria, cv2.MORPH_CLOSE, kernel, iterations=1
    )

    carpeta_salida.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(carpeta_salida / "original-binarizada.png"), original_binaria)
    cv2.imwrite(str(carpeta_salida / "apertura.png"), imagen_apertura)
    cv2.imwrite(str(carpeta_salida / "cierre.png"), imagen_cierre)

    print("Kernel utilizado:\n", kernel)
    print("Pixeles blancos - original:", np.count_nonzero(original_binaria))
    print("Pixeles blancos - apertura:", np.count_nonzero(imagen_apertura))
    print("Pixeles blancos - cierre:", np.count_nonzero(imagen_cierre))
    print(f"Resultados guardados en: {carpeta_salida}")
    print("La apertura elimina ruido externo; el cierre rellena pequenos huecos internos.")


if __name__ == "__main__":
    main()
