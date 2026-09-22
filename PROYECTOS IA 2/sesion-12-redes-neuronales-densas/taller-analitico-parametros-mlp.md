# SESIÓN 12 REDES NEURONALES DENSAS O MULTICAPA

## Taller analítico: contando parámetros

Diseñamos una red neuronal para aprobar tarjetas de crédito con:

- 3 entradas: Edad, Ingresos y Deuda.
- 1 capa oculta con 4 neuronas.
- 1 neurona en la capa de salida.

Cada conexión tiene un peso y cada neurona tiene un sesgo. Por eso, el conteo incluye las conexiones entre capas y los sesgos de las neuronas.

### 1. Pesos entre la capa de entrada y la capa oculta

Cada una de las 3 entradas se conecta con las 4 neuronas ocultas:

```text
3 entradas × 4 neuronas = 12 pesos
```

La matriz de esta conexión tiene dimensión `3 × 4`.

### 2. Sesgos de la capa oculta

Cada neurona oculta tiene un sesgo:

```text
4 neuronas ocultas × 1 sesgo = 4 sesgos
```

### 3. Pesos y sesgo entre la capa oculta y la capa de salida

Las 4 neuronas ocultas se conectan con la única neurona de salida:

```text
4 neuronas × 1 salida = 4 pesos
```

La matriz de esta conexión tiene dimensión `4 × 1`.

La neurona de salida tiene un sesgo:

```text
1 sesgo
```

### 4. Total de parámetros entrenables

```text
12 pesos + 4 sesgos + 4 pesos + 1 sesgo = 21 parámetros
```

La red tiene **21 parámetros entrenables** en total.

Estos parámetros son los valores que el modelo ajustaría durante el entrenamiento.
