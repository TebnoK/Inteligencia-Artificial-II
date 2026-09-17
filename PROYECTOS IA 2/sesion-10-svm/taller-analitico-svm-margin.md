# TALLER ANALÍTICO: DIBUJANDO EL MARGEN 

1. Para ubicar la línea, se comparan los puntos más cercanos de las dos clases:

	- Clase A: (3,3) y (4,2) → **x + y = 6**.
	- Clase B: (6,6) → **x + y = 12**.

	La línea óptima queda justo en la mitad:

	**(6 + 12) / 2 = 9**

	Por tanto, la frontera es **x + y = 9**. Las líneas de margen son **x + y = 6** y **x + y = 12**, con la misma distancia respecto a la frontera.

2. Los vectores de soporte son **(3,3), (4,2) y (6,6)**, porque son los puntos que quedan sobre las líneas de margen:

	- (3,3) y (4,2) → **3 + 3 = 4 + 2 = 6**.
	- (6,6) → **6 + 6 = 12**.

3. **No cambiaría la posición de la línea**. El nuevo punto cumple:

	**1 + 1 = 2**

	Como queda por debajo de la línea de margen de la Clase A (**x + y = 6**) y no es un vector de soporte, no modifica la frontera **x + y = 9**.
