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

## Autor

Jhon Esteban Monroy Trujillo — Ingeniería de Sistemas
