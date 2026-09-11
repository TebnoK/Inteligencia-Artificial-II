# Taller Analítico 1: Indexación y Tensores

**Sesión 1 — Refuerzo Python y Álgebra Lineal · Inteligencia Artificial II**

## Matriz de referencia (A, 5x5)

```
    j=0  j=1  j=2  j=3  j=4
i=0   0  255  255  255    0
i=1 255    0    0    0  255
i=2 255    0  128    0  255
i=3 255    0    0    0  255
i=4   0  255  255  255    0
```

## 1. Valor exacto de A[2,3]

Con índice base 0, la fila `i=2` es `[255, 0, 128, 0, 255]`. El elemento en la columna `j=3` de esa fila es:

**A[2,3] = 0**

**Qué representa visualmente:** es un píxel negro puro (intensidad mínima, 8 bits). Se ubica justo a la derecha del píxel gris central (A[2,2] = 128), formando parte del anillo negro que separa el centro gris del marco blanco exterior de la imagen.

## 2. Bytes almacenados en un tensor RGB de 1080 x 1920 x 3

Cada canal de color aporta una matriz M x N independiente, así que el total de valores individuales es el producto de las tres dimensiones:

```
1080 × 1920 × 3 = 6 220 800 valores (bytes), uno por canal y por píxel
```

Como cada valor ocupa 1 byte (rango [0, 255], 8 bits):

**6 220 800 bytes ≈ 6 075 KB ≈ 5.93 MB** sin comprimir, para una sola imagen.
