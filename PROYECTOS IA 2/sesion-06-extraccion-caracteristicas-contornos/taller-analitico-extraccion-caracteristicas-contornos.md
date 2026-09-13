# TALLER ANALÍTICO: BOUNDING BOX 

Supongamos que el algoritmo detectó un contorno con las siguientes 4 coordenadas (esquinas de un objeto irregular):

$$
A(2, 4), \quad B(8, 2), \quad C(10, 7), \quad D(3, 9)
$$

1. Un Bounding Box (caja delimitadora) es el rectángulo no rotado más pequeño que encierra completamente al objeto. Para calcularlo, debemos hallar las coordenadas extremas:
   $$
   (X_{min}, Y_{min}, X_{max}, Y_{max})
   $$
   Determine analíticamente estos 4 valores.

2. Calcule el ancho $W$ y el alto $H$ del Bounding Box.

## Solución

Tomamos las coordenadas del contorno:

- $A(2, 4)$
- $B(8, 2)$
- $C(10, 7)$
- $D(3, 9)$

### 1. Coordenadas extremas

Para hallar la caja delimitadora, se toman los mínimos y máximos de las coordenadas x e y:

- $X_{min} = \min(2, 8, 10, 3) = 2$
- $Y_{min} = \min(4, 2, 7, 9) = 2$
- $X_{max} = \max(2, 8, 10, 3) = 10$
- $Y_{max} = \max(4, 2, 7, 9) = 9$

Entonces, el Bounding Box queda definido como:

$$
(X_{min}, Y_{min}, X_{max}, Y_{max}) = (2, 2, 10, 9)
$$

### 2. Ancho y alto

El ancho se calcula como la diferencia entre el máximo y el mínimo en x:

$$
W = X_{max} - X_{min} = 10 - 2 = 8
$$

El alto se calcula como la diferencia entre el máximo y el mínimo en y:

$$
H = Y_{max} - Y_{min} = 9 - 2 = 7
$$

## Resultado final

- $X_{min} = 2$
- $Y_{min} = 2$
- $X_{max} = 10$
- $Y_{max} = 9$
- $W = 8$
- $H = 7$




