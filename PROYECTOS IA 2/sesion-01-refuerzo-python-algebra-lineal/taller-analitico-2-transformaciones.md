# Taller Analítico 2: Transformaciones

**Sesión 1 — Refuerzo Python y Álgebra Lineal · Inteligencia Artificial II**

## 1. Transpuesta de la matriz identidad I (4x4)

**Resultado: I⁴ˣ⁴ᵀ = I⁴ˣ⁴** (la transpuesta es la misma matriz identidad).

**Explicación geométrica:** transponer refleja la matriz sobre su diagonal principal (intercambia fila i por columna j). En la identidad, los únicos valores distintos de cero (los 1) están exactamente sobre esa diagonal. Reflejar la matriz sobre la propia línea en la que viven sus valores no mueve nada: cada 1 se refleja sobre sí mismo. Por eso la identidad es una matriz **simétrica**, invariante ante la transposición.

## 2. Neuronas de entrada tras aplanar una imagen (200, 200, 3)

El aplanamiento (`flatten`) convierte un tensor M x N x C en un vector de tamaño (M·N·C) x 1:

```
200 × 200 × 3 = 120 000
```

**La capa de entrada necesita exactamente 120 000 neuronas** para recibir el vector completo sin pérdida de información.
