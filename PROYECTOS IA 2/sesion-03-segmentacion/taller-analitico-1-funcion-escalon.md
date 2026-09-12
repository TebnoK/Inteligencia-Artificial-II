# Taller Analitico 1: Funcion Escalon

**Sesion 3 - Segmentacion - Inteligencia Artificial II**

## 1. Umbralizacion binaria con `T = 135`

La regla es:

```text
f(x, y) = 255, si I(x, y) >= 135
f(x, y) = 0,   si I(x, y) < 135
```

Aplicando la regla a la matriz:

```text
80   120  140
90   200  210
50   130  250
```

se obtiene:

```text
0    0    255
0    255  255
0    0    255
```

Los valores `140`, `200`, `210` y `250` se convierten en blanco porque son mayores o iguales que `135`. Los restantes se convierten en negro.

## 2. Error de elegir `T = 135` cuando se querian aislar valores mayores que 100

Con el objetivo de conservar todos los valores mayores que `100`, la matriz esperada seria:

```text
0    255  255
0    255  255
0    255  255
```

El umbral `135` deja fuera incorrectamente los valores `120` y `130`, que si son mayores que `100`. En la imagen segmentada esto puede producir huecos o partes desaparecidas dentro del objeto de interes. El objeto quedaria incompleto y su forma podria fragmentarse.

La eleccion de un umbral debe corresponder al criterio de separacion buscado: si el limite es `100`, una implementacion con la regla `>=` debe usar `T = 101` para representar estrictamente los valores mayores que `100`, o usar directamente una comparacion `imagen > 100`.
