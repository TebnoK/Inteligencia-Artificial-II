"""
Taller de Laboratorio 1: Umbralizacion y metodo de Otsu
Sesion 3 - Segmentacion - Inteligencia Artificial II

Compara una umbralizacion fija con Otsu. Usa una imagen sintetica si no se
proporciona una ruta. Los resultados se pueden guardar en una carpeta.
"""
import sys
from pathlib import Path

import cv2
import numpy as np


def crear_imagen_prueba():
    """Genera un objeto claro sobre un fondo oscuro con ruido puntual."""
    imagen = np.full((160, 240), 45, dtype=np.uint8)
    cv2.rectangle(imagen, (55, 35), (185, 125), 200, -1)
    imagen[20, 30] = 220
    imagen[140, 210] = 230
    imagen[70, 120] = 20
    return imagen


def cargar_imagen(ruta):
    imagen = cv2.imread(str(ruta), cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise SystemExit(f"No se pudo leer la imagen: {ruta}")
    return imagen


def guardar_resultados(imagen, binaria_fija, binaria_otsu, carpeta):
    carpeta.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(carpeta / "imagen-grises.png"), imagen)
    cv2.imwrite(str(carpeta / "umbral-fijo.png"), binaria_fija)
    cv2.imwrite(str(carpeta / "umbral-otsu.png"), binaria_otsu)


def main():
    ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    carpeta_salida = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else Path(__file__).resolve().parent / "resultados-sesion-03"
    )
    imagen = cargar_imagen(ruta) if ruta else crear_imagen_prueba()

    umbral_fijo, imagen_binaria = cv2.threshold(
        imagen, 127, 255, cv2.THRESH_BINARY
    )
    umbral_otsu, imagen_otsu = cv2.threshold(
        imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    guardar_resultados(imagen, imagen_binaria, imagen_otsu, carpeta_salida)
    print(f"Umbral fijo utilizado: {umbral_fijo}")
    print(f"Umbral optimo calculado por Otsu: {umbral_otsu}")
    print(f"Resultados guardados en: {carpeta_salida}")


if __name__ == "__main__":
    main()
