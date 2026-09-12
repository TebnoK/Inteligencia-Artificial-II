# Taller Analitico: Calculando la Convolucion

**Sesion 4 - Convolucion - Inteligencia Artificial II**

## 1. Nuevo valor del pixel central

La region de imagen es:

```text
10   20   30
15  250   15
20   10   20
```

El kernel de media 3x3 asigna `1/9` a cada posicion. Por tanto, el producto punto es:

```text
(10 + 20 + 30 + 15 + 250 + 15 + 20 + 10 + 20) / 9
= 390 / 9
= 43.333333...
```

El nuevo valor del pixel central es aproximadamente **43.33**. Si se almacena como intensidad entera de 8 bits, puede redondearse a `43`.

## 2. Por que el filtro de media suaviza la imagen

El valor anomalo `250` deja de controlar por si solo el pixel central. Se suma con los otros ocho vecinos y la suma se reparte entre las nueve posiciones. La intensidad baja de `250` a aproximadamente `43.33`, mucho mas cercana a los valores oscuros del vecindario.

El proceso se llama difusion o suavizado porque reemplaza cada pixel por un promedio local. Reduce variaciones bruscas y ruido, aunque tambien puede difuminar bordes reales: para el filtro de media todos los vecinos tienen el mismo peso.
