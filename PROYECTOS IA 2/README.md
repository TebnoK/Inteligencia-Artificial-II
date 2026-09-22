# Inteligencia Artificial II — Talleres

Repositorio de talleres semanales de la asignatura **Inteligencia Artificial II** (V semestre, Ingeniería de Sistemas), Institución Universitaria de Colombia. Docente: Amaury Giovanni Méndez Aguirre.

Cada carpeta `sesion-XX-.../` corresponde a una clase e incluye dos tipos de entregable:

- **Talleres analíticos** (`.md`): preguntas teóricas con su justificación matemática.
- **Talleres de laboratorio** (`.py`): retos de código resueltos en Python/NumPy.

## Sesiones

| # | Tema | Talleres |
|---|---|---|
| 01 | Refuerzo Python y Álgebra Lineal | [Analítico 1](sesion-01-refuerzo-python-algebra-lineal/taller-analitico-1-indexacion-tensores.md) · [Analítico 2](sesion-01-refuerzo-python-algebra-lineal/taller-analitico-2-transformaciones.md) · [Laboratorio 1](sesion-01-refuerzo-python-algebra-lineal/taller-laboratorio-1-transformaciones-afines.py) · [Laboratorio final](sesion-01-refuerzo-python-algebra-lineal/taller-laboratorio-final-kernel.py) |
| 02 | Tensor de color y análisis estadístico | [Analítico 1](sesion-02-tensor-color-analisis-estadistico/taller-analitico-1-slicing-tensores.md) · [Laboratorio 1](sesion-02-tensor-color-analisis-estadistico/taller-laboratorio-1-escala-grises.py) · [Laboratorio 2](sesion-02-tensor-color-analisis-estadistico/taller-laboratorio-2-histogramas.py) |
| 03 | Segmentación | [Analítico 1](sesion-03-segmentacion/taller-analitico-1-funcion-escalon.md) · [Laboratorio 1](sesion-03-segmentacion/taller-laboratorio-1-umbralizacion.py) · [Laboratorio final](sesion-03-segmentacion/taller-laboratorio-final-morfologia.py) |
| 04 | Convolución | [Analítico](sesion-04-convolucion/taller-analitico-calculando-convolucion.md) · [Laboratorio final](sesion-04-convolucion/taller-laboratorio-final-filtros.py) |
| 05 | Gradientes espaciales y detección de bordes | [Analítico](sesion-05-gradientes-bordes/taller-analitico-calculando-gradiente.md) · [Laboratorio final](sesion-05-gradientes-bordes/taller-laboratorio-final-inspector-bordes.py) |
| 06 | Extracción de características y contornos | [Analítico](sesion-06-extraccion-caracteristicas-contornos/taller-analitico-extraccion-caracteristicas-contornos.md) · [Laboratorio final](sesion-06-extraccion-caracteristicas-contornos/taller-laboratorio-final-contornos-monedas.py) |
| 09 | K-Vecinos más cercanos (KNN) | [Analítico](sesion-09-knn/taller-analitico-knn.md) · [Laboratorio final](sesion-09-knn/taller-laboratorio-final-knn.py) |
| 10 | Support Vector Machine (SVM) | [Analítico](sesion-10-svm/taller-analitico-svm-margin.md) · [Laboratorio final](sesion-10-svm/taller-laboratorio-final-svm.py) |
| 11 | Redes neuronales: el perceptrón | [Analítico](sesion-11-redes-neuronales/taller-analitico-perceptron.md) · [Laboratorio final](sesion-11-redes-neuronales/taller-laboratorio-final-perceptron.py) |


## Requisitos

- Python 3.10+  

```bash
pip install -r requirements.txt
```

## Ejecución de un taller de laboratorio

```bash
python sesion-01-refuerzo-python-algebra-lineal/taller-laboratorio-1-transformaciones-afines.py
```

Los laboratorios de la sesión 2 usan una imagen de prueba si no se proporciona
una ruta. Para analizar una imagen propia:

```bash
python sesion-02-tensor-color-analisis-estadistico/taller-laboratorio-1-escala-grises.py ruta/a/imagen.jpg
python sesion-02-tensor-color-analisis-estadistico/taller-laboratorio-2-histogramas.py ruta/a/imagen.jpg
```

Los laboratorios de la sesión 3 guardan sus resultados en
`sesion-03-segmentacion/resultados-sesion-03/`.
Se puede indicar una imagen en escala de grises y una carpeta de salida:

```bash
python sesion-03-segmentacion/taller-laboratorio-1-umbralizacion.py ruta/documento.jpg resultados-sesion-03
python sesion-03-segmentacion/taller-laboratorio-final-morfologia.py ruta/documento.jpg resultados-sesion-03
```
El laboratorio de la sesión 4 genera automáticamente una imagen con ruido de
sal y pimienta. No requiere descargar una imagen; opcionalmente se puede pasar
una imagen en escala de grises y una carpeta de salida:

```bash
python sesion-04-convolucion/taller-laboratorio-final-filtros.py
python sesion-04-convolucion/taller-laboratorio-final-filtros.py ruta/imagen.jpg resultados-sesion-04
```
Para la sesión 5, se coloca una imagen real con formas y texturas en
`sesion-05-gradientes-bordes/imagenes/` con el nombre `imagen-bordes.jpg`
de un fondo con formas geometricas de edificios.
Después ejecuta: 

```bash
python sesion-05-gradientes-bordes/taller-laboratorio-final-inspector-bordes.pyy 
```

Los resultados se guardan en `sesion-05-gradientes-bordes/resultados-sesion-05/`.

```bash
python sesion-05-gradientes-bordes/taller-laboratorio-final-inspector-bordes.py ruta/imagen.jpg resultados-sesion-05
```
Para la sesión 6, la imagen de monedas se guarda en
`sesion-06-extraccion-caracteristicas-contornos/imagenes/` usando un nombre
como `monedas.jpg` o `imagen-monedas.jpg`.

```bash
python sesion-06-extraccion-caracteristicas-contornos/taller-laboratorio-final-contornos-monedas.py
```

Los resultados se guardan en
`sesion-06-extraccion-caracteristicas-contornos/resultados-sesion-06/`.

Para la sesión 9, el laboratorio usa el conjunto Iris para entrenar un
clasificador KNN y medir su precisión. Se ejecuta con:

```bash
python sesion-09-knn/taller-laboratorio-final-knn.py
```

El análisis se hace directamente sobre los datos del conjunto `iris`.

Para la sesión 10, el laboratorio construye un conjunto bidimensional con dos
clases y entrena un SVM con kernel lineal para visualizar la frontera y el
margen máximo. Se ejecuta con:

```bash
python sesion-10-svm/taller-laboratorio-final-svms.py
```
Para la sesión 11, el laboratorio implementa un perceptrón desde cero y modifica manualmente sus pesos para resolver la compuerta OR:

```bash
python sesion-11-redes-neuronales/taller-laboratorio-final-perceptron.py
```


## Autor

Jhon Esteban Monroy Trujillo — Ingeniería de Sistemas
