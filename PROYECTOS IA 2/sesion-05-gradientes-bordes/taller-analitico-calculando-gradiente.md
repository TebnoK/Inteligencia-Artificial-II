# Taller Analitico: Calculando el Gradiente

**Sesion 5 - Gradientes espaciales y deteccion de bordes - Inteligencia Artificial II**

## Matriz de imagen

```text
0    0    255
0    0    255
0    0    255
```

## 1. Convolucion con Sobel X

El kernel Sobel X es:

```text
-1   0   1
-2   0   2
-1   0   1
```

El producto elemento a elemento y la suma son:

```text
(0*-1) + (0*0) + (255*1)
+ (0*-2) + (0*0) + (255*2)
+ (0*-1) + (0*0) + (255*1)
= 255 + 510 + 255
= 1020
```

Por tanto, el gradiente horizontal en el pixel central es **Gx = 1020**. El valor alto aparece porque la intensidad cambia bruscamente de negro a blanco en la direccion horizontal.

## 2. Convolucion con Sobel Y

El kernel Sobel Y es:

```text
-1  -2  -1
 0   0   0
 1   2   1
```

La fila superior y la fila inferior de la imagen son iguales. Al aplicar el kernel, los aportes se cancelan:

```text
(-1*0) + (-2*0) + (-1*255)
+ (0*0) + (0*0) + (0*255)
+ (1*0) + (2*0) + (1*255)
= -255 + 255
= 0
```

Por tanto, **Gy = 0**. La imagen no cambia verticalmente: el borde es vertical y se extiende de arriba abajo. El gradiente detectado queda en el eje X.

## Magnitud del gradiente

```text
G = sqrt(Gx^2 + Gy^2)
  = sqrt(1020^2 + 0^2)
  = 1020
```

En una imagen de 8 bits, este resultado suele convertirse con valor absoluto y escala para poder visualizarlo sin desbordamiento.
