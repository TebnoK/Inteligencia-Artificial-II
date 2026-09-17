# Taller analítico: la votación espacial (25 min)

Un sistema debe clasificar si un cliente comprará un producto basándose en dos características: $X = $ Edad, $Y = $ Salario en miles. Tenemos 3 clientes históricos (Dataset):

- Cliente 1: $A(20, 30)$ → Clase: NO COMPRA
- Cliente 2: $B(40, 50)$ → Clase: COMPRA
- Cliente 3: $C(35, 45)$ → Clase: COMPRA

Llega un nuevo cliente desconocido: Punto Nuevo $(40, 40)$.

## 1. Calcule matemáticamente la Distancia Euclidiana desde el Punto Nuevo hasta A, B y C.

La fórmula de la distancia euclidiana entre dos puntos $(x_1, y_1)$ y $(x_2, y_2)$ es:

$$
 d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 }
$$

### Distancia al cliente A

$$
 d(A, N) = \sqrt{(40 - 20)^2 + (40 - 30)^2 }
 = \sqrt{20^2 + 10^2}
 = \sqrt{400 + 100}
 = \sqrt{500}
 \approx 22.36
$$

### Distancia al cliente B

$$
 d(B, N) = \sqrt{(40 - 40)^2 + (40 - 50)^2 }
 = \sqrt{0^2 + (-10)^2}
 = \sqrt{100}
 = 10
$$

### Distancia al cliente C

$$
 d(C, N) = \sqrt{(40 - 35)^2 + (40 - 45)^2 }
 = \sqrt{5^2 + (-5)^2}
 = \sqrt{25 + 25}
 = \sqrt{50}
 \approx 7.07
$$

## 2. Si definimos $K = 1$, ¿cuál será la clasificación del nuevo cliente?

Con $K = 1$, se toma el vecino más cercano al punto nuevo.

Los vecinos y sus distancias son:

- $A$: $22.36$ → NO COMPRA
- $B$: $10$ → COMPRA
- $C$: $7.07$ → COMPRA

El vecino más cercano es $C$, y como $C$ pertenece a la clase COMPRA, entonces:

- La clasificación con $K = 1$ es: COMPRA.

## 3. Si definimos $K = 3$, ¿cuál será la clasificación? ¿Hubo un cambio en la decisión?

Con $K = 3$, se consideran los tres vecinos más cercanos: $C$, $B$ y $A$.

Sus clases son:

- $C$ → COMPRA
- $B$ → COMPRA
- $A$ → NO COMPRA

La votación es:

- COMPRA: 2 votos
- NO COMPRA: 1 voto

Por lo tanto, la predicción con $K = 3$ también es:

- COMPRA.

No hubo cambio en la decisión: en ambos casos el nuevo cliente se clasifica como COMPRA.

## Respuesta final

- Distancias: $d(A,N) \approx 22.36$, $d(B,N)=10$, $d(C,N) \approx 7.07$
- Con $K=1$: COMPRA
- Con $K=3$: COMPRA
- No cambió la decisión.

### Espacio para cálculo de distancias (raíces cuadradas)

$$
\text{A: } \sqrt{(40-20)^2 + (40-30)^2} = \sqrt{500} \approx 22.36
$$

$$
\text{B: } \sqrt{(40-40)^2 + (40-50)^2} = \sqrt{100} = 10
$$

$$
\text{C: } \sqrt{(40-35)^2 + (40-45)^2} = \sqrt{50} \approx 7.07
$$
