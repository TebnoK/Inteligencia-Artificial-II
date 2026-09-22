# SESIÓN 11 REDES NEURONALES -- EL PERCEPTRÓN --

## Taller analítico: calculando el disparo

El perceptrón combina las entradas, sus pesos y un sesgo para obtener un valor `Z`. Luego aplica una función de activación que decide si la neurona se dispara.

Datos del cliente:

- Ingresos: `X1 = 50`
- Deudas: `X2 = 20`
- Peso de ingresos: `W1 = 0.8`
- Peso de deudas: `W2 = -0.5`
- Sesgo: `b = -10`

### 1. Cálculo de la combinación lineal

La ecuación es:

```text
Z = (X1 * W1) + (X2 * W2) + b
```

Reemplazando los valores:

```text
Z = (50 * 0.8) + (20 * -0.5) - 10
Z = 40 - 10 - 10
Z = 20
```

### 2. Función de activación

La función escalón indica:

```text
Salida = 1, si Z >= 0
Salida = 0, si Z < 0
```

Como `Z = 20` y `20 >= 0`:

```text
Salida = 1
```

La neurona dispara y aprueba el crédito.

El valor positivo de `Z` indica que, con estos datos y estos parámetros, la combinación supera el umbral de activación.

### 3. Análisis del peso W2

El peso `W2 = -0.5` tiene sentido porque representa las deudas. Al aumentar las deudas, el término `(X2 * W2)` disminuye el valor de `Z`, reduciendo la posibilidad de aprobar el crédito.

El peso positivo de los ingresos produce el efecto contrario: al aumentar `X1`, también aumenta `Z` y se favorece la activación de la neurona.
