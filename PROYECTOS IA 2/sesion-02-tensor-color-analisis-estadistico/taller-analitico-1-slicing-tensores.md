# Taller Analitico 1: Operaciones con Tensores

**Sesion 2 - Tensor de color y analisis estadistico - Inteligencia Artificial II**

## 1. Dimensiones y contenido del recorte

La instruccion es:

```python
recorte = imagen[100:200, 300:400, 1]
```

Para una imagen de `1920 x 1080` en formato `(alto, ancho, canales)`, el slicing selecciona:

- Filas desde `100` hasta `199`: `100` filas.
- Columnas desde `300` hasta `399`: `100` columnas.
- Canal `1`: un unico canal, el canal verde en el orden BGR de OpenCV.

Por tanto:

```text
recorte.shape == (100, 100)
```

El resultado es una matriz bidimensional con la intensidad del canal verde de cada pixel ubicado en el rectangulo comprendido entre esas filas y columnas. No contiene los tres canales ni una imagen RGB completa.

## 2. Por que slicing es mas eficiente que dos ciclos `for`

La expresion:

```python
canal_azul = imagen[:, :, 0]
```

usa operaciones vectorizadas de NumPy. La seleccion se ejecuta en codigo interno optimizado y, normalmente, devuelve una vista sobre la memoria original en lugar de copiar pixel por pixel.

En cambio, dos ciclos `for` hacen que Python interprete una instruccion por cada coordenada de la imagen. Esto agrega el costo de millones de iteraciones, accesos y comprobaciones individuales.

La ventaja no es solo que se escriba menos codigo: NumPy aprovecha memoria contigua y operaciones compiladas sobre bloques de datos. Ademas, al ser una vista, el slicing puede evitar una copia; por eso conviene usar `.copy()` unicamente cuando se necesite modificar el canal sin alterar la imagen original.

> Nota: en OpenCV el orden de los canales es BGR: `0 = azul`, `1 = verde`, `2 = rojo`.
