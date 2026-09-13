"""
Taller de Laboratorio: Extracción de características y contornos
Sesión 6 - Inteligencia Artificial II

Objetivo:
- cargar una imagen con monedas,
- binarizar la imagen para separar fondo y objetos,
- detectar contornos y calcular propiedades geométricas,
- guardar resultados visuales en una carpeta de salida.
"""

import sys
from pathlib import Path

import cv2
import numpy as np

CARPETA_SESION = Path(__file__).resolve().parent
CARPETA_IMAGENES = CARPETA_SESION / "imagenes"
CARPETA_SALIDA = CARPETA_SESION / "resultados-sesion-06"
EXTENSIONES_VALIDAS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def buscar_rutas_imagenes():
    """Busca las imágenes disponibles y devuelve como máximo las dos primeras."""
    nombres_preferidos = [
        "monedas.jpg",
        "imagen-monedas.jpg",
        "imagen_monedas.jpg",
        "coins.jpg",
        "monedas.png",
        "imagen-monedas.png",
        "imagen_monedas.png",
        "monedas.jpeg",
        "imagen-monedas.jpeg",
        "imagen_monedas.jpeg",
    ]
    rutas = []
    for nombre in nombres_preferidos:
        ruta = CARPETA_IMAGENES / nombre
        if ruta.exists() and ruta not in rutas:
            rutas.append(ruta)

    for ruta in sorted(CARPETA_IMAGENES.iterdir()):
        if ruta.is_file() and ruta.suffix.lower() in EXTENSIONES_VALIDAS and ruta not in rutas:
            rutas.append(ruta)

    return rutas[:2]


def cargar_imagen(ruta=None):
    """Carga una imagen desde la carpeta de imagenes o desde una ruta dada."""
    if ruta is None:
        rutas = buscar_rutas_imagenes()
        ruta = rutas[0] if rutas else None
        if ruta is None:
            raise SystemExit(
                "No se encontró la imagen de monedas. Colócala en "
                f"'{CARPETA_IMAGENES}' con nombres como monedas.jpg o imagen-monedas.jpg"
            )

    imagen = cv2.imread(str(ruta), cv2.IMREAD_COLOR)
    if imagen is None:
        raise SystemExit(f"No se pudo leer la imagen: {ruta}")
    return imagen


def preparar_imagen(imagen):
    """Convierte a gris y mejora el contraste para facilitar la segmentación."""
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (5, 5), 0)
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return gris, binaria


def detectar_contornos(binaria):
    """Obtiene contornos exteriores relevantes y descarta ruido de la imagen."""
    contornos, jerarquia = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    alto, ancho = binaria.shape
    contornos_validos = []
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        x, y, w, h = cv2.boundingRect(contorno)
        toca_borde = x == 0 or y == 0 or x + w >= ancho or y + h >= alto
        if area >= 1000 and not toca_borde:
            contornos_validos.append(contorno)
    return contornos_validos, jerarquia


def dibujar_contornos(imagen, contornos):
    """Dibuja los contornos sobre una copia de la imagen original."""
    resultado = imagen.copy()
    cv2.drawContours(resultado, contornos, -1, (0, 255, 0), 2)
    return resultado


def analizar_contornos(imagen, contornos):
    """Calcula propiedades geométricas básicas para cada contorno."""
    datos = []
    for idx, contorno in enumerate(contornos):
        area = cv2.contourArea(contorno)
        perimetro = cv2.arcLength(contorno, True)
        x, y, w, h = cv2.boundingRect(contorno)
        momento = cv2.moments(contorno)
        if momento["m00"] != 0:
            cx = momento["m10"] / momento["m00"]
            cy = momento["m01"] / momento["m00"]
        else:
            cx, cy = 0, 0

        datos.append(
            {
                "indice": idx,
                "area": area,
                "perimetro": perimetro,
                "bbox": (x, y, w, h),
                "centroide": (cx, cy),
            }
        )

    return datos


def guardar_resultados(imagen, gris, binaria, contornos, datos, carpeta_salida):
    """Guarda la imagen original, la binaria y un panel con contornos."""
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(str(carpeta_salida / "original.png"), imagen)
    cv2.imwrite(str(carpeta_salida / "gris.png"), gris)
    cv2.imwrite(str(carpeta_salida / "binaria.png"), binaria)

    contornos_visual = dibujar_contornos(imagen, contornos)
    cv2.imwrite(str(carpeta_salida / "contornos-detectados.png"), contornos_visual)

    panel = np.hstack([imagen, contornos_visual])
    cv2.imwrite(str(carpeta_salida / "panel-comparativo.png"), panel)

    with open(carpeta_salida / "analisis-contornos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Análisis de contornos\n")
        archivo.write("====================\n\n")
        for item in datos:
            archivo.write(
                f"Contorno {item['indice']}: area={item['area']:.2f}, "
                f"perimetro={item['perimetro']:.2f}, "
                f"bbox={item['bbox']}, centroide={item['centroide']}\n"
            )

    print(f"Imagen procesada: {imagen.shape[:2]}")
    print(f"Se detectaron {len(contornos)} contornos.")
    print(f"Resultados guardados en: {carpeta_salida}")


def main():
    rutas = [Path(argumento) for argumento in sys.argv[1:]]
    if not rutas:
        rutas = buscar_rutas_imagenes()
    if len(rutas) < 2:
        raise SystemExit("Se necesitan al menos dos imágenes en la carpeta imagenes.")

    for ruta in rutas:
        imagen = cargar_imagen(ruta)
        gris, binaria = preparar_imagen(imagen)
        contornos, _ = detectar_contornos(binaria)
        datos = analizar_contornos(imagen, contornos)
        carpeta_salida = CARPETA_SALIDA / ruta.stem
        guardar_resultados(imagen, gris, binaria, contornos, datos, carpeta_salida)


if __name__ == "__main__":
    main()
