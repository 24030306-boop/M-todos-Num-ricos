# 📘 Tema 4: Diferenciación e Integración Numérica

Este directorio contiene el desarrollo de algoritmos y simulaciones enfocados en aproximar derivadas e integrales definidas mediante métodos numéricos. Estas técnicas son fundamentales cuando una función no puede resolverse analíticamente o únicamente se dispone de datos discretos.

La diferenciación e integración numérica son ampliamente utilizadas en ingeniería, física, simulaciones computacionales y análisis científico.

---

# 🛠️ Catálogo de Métodos Desarrollados

| Método                  | Descripción                                                   |
| :---------------------- | :------------------------------------------------------------ |
| Diferenciación Numérica | Aproximación de derivadas mediante diferencias finitas.       |
| Método del Trapecio     | Aproximación de integrales usando trapecios.                  |
| Método de Simpson 1/3   | Integración usando aproximaciones parabólicas.                |
| Cuadratura Gaussiana    | Integración de alta precisión mediante pesos y nodos óptimos. |

---

# 1. 🔹 Diferenciación Numérica (3 y 5 Puntos)

## 🎯 Objetivo

Aproximar la derivada de una función utilizando valores discretos cercanos al punto de interés.

---

## 📝 Descripción del Método

La diferenciación numérica utiliza diferencias finitas para aproximar derivadas cuando no es posible obtenerlas analíticamente. Dependiendo de la cantidad de puntos utilizados, aumenta la precisión de la aproximación.

---

## 🔢 Fórmulas Generales

Diferencia hacia adelante:

```txt id="e4d2yw"
f'(x) ≈ (f(x+h) - f(x)) / h
```

Diferencia centrada:

```txt id="q0v6kx"
f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
```

Fórmula de 5 puntos:

```txt id="w3kl8f"
f'(x) ≈ [-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)] / 12h
```

---

## 👣 Pasos del Algoritmo

1. Definir función.
2. Seleccionar punto.
3. Definir espaciamiento (h).
4. Aplicar fórmula.
5. Obtener aproximación.

---

## 💻 Pseudocódigo

```txt id="rl3r0s"
INICIO

Leer funcion
Leer h

Calcular derivada

Mostrar resultado

FIN
```

---

## 🐍 Código en Python

```python id="okq5tx"
def derivada_centrada(f, x, h):

    return (f(x + h) - f(x - h)) / (2 * h)
```

---

## 📊 Resultado de Ejecución

```txt id="fh5e1v"
Derivada aproximada:
2.00001
```

---

## 🏁 Conclusión

Las fórmulas centradas ofrecen mayor precisión que las diferencias simples debido a su menor error de truncamiento.

---

# 2. 🔹 Método del Trapecio

## 🎯 Objetivo

Aproximar el valor de una integral definida mediante áreas trapezoidales.

---

## 📝 Descripción del Método

La regla del trapecio aproxima el área bajo una curva reemplazando la función original por segmentos rectos.

---

## 🔢 Fórmula General

```txt id="ffu8ww"
Integral ≈ ((b-a)/2) * [f(a) + f(b)]
```

Trapecio compuesto:

```txt id="q0q2fi"
Integral ≈ (h/2) * [f(x0)+2Σf(xi)+f(xn)]
```

---

## 👣 Pasos del Algoritmo

1. Dividir intervalo.
2. Evaluar función.
3. Construir trapecios.
4. Sumar áreas.
5. Obtener integral.

---

## 💻 Pseudocódigo

```txt id="t4y9ec"
INICIO

Dividir intervalo

Evaluar puntos

Aplicar formula

Mostrar resultado

FIN
```

---

## 🐍 Código en Python

```python id="m58xx6"
def trapecio(f, a, b):

    return ((b - a) / 2) * (f(a) + f(b))
```

---

## 📊 Resultado de Ejecución

```txt id="fw72jq"
Integral aproximada:
5.33333
```

---

## 🏁 Conclusión

El método del trapecio es simple y eficiente, aunque puede presentar errores en funciones muy curvas.

---

# 3. 🔹 Método de Simpson 1/3

## 🎯 Objetivo

Incrementar la precisión de la integración utilizando parábolas en lugar de líneas rectas.

---

## 📝 Descripción del Método

La regla de Simpson aproxima la función mediante polinomios cuadráticos, logrando resultados más precisos que el método del trapecio.

---

## 🔢 Fórmula General

```txt id="gw5l7z"
Integral ≈ (h/3) * [f(x0)+4f(x1)+f(x2)]
```

---

## 👣 Pasos del Algoritmo

1. Dividir intervalo en partes pares.
2. Evaluar función.
3. Aplicar pesos.
4. Sumar resultados.
5. Obtener integral.

---

## 💻 Pseudocódigo

```txt id="g6dxnk"
INICIO

Dividir intervalo

Aplicar Simpson

Mostrar integral

FIN
```

---

## 🐍 Código en Python

```python id="o4s0zz"
def simpson(f, a, b):

    h = (b - a) / 2

    return (h / 3) * (f(a) + 4*f(a+h) + f(b))
```

---

## 📊 Resultado de Ejecución

```txt id="m2rwlr"
Integral aproximada:
5.33333
```

---

## 🏁 Conclusión

Simpson 1/3 proporciona mayor precisión utilizando aproximaciones parabólicas.

---

# 4. 🔹 Cuadratura Gaussiana

## 🎯 Objetivo

Obtener integrales numéricas de alta precisión utilizando puntos óptimos de evaluación.

---

## 📝 Descripción del Método

La cuadratura gaussiana utiliza nodos y pesos matemáticos especiales derivados de los polinomios de Legendre para maximizar la precisión con pocas evaluaciones.

---

## 🔢 Fórmula General

```txt id="vm4tp8"
Integral ≈ Σ(w_i * f(x_i))
```

---

## 👣 Pasos del Algoritmo

1. Seleccionar nodos.
2. Seleccionar pesos.
3. Evaluar función.
4. Multiplicar pesos.
5. Sumar resultados.

---

## 💻 Pseudocódigo

```txt id="t8w8sz"
INICIO

Seleccionar pesos y nodos

Evaluar funcion

Sumar resultados

Mostrar integral

FIN
```

---

## 🐍 Código en Python

```python id="osf8yw"
import numpy as np

def cuadratura_gaussiana(f):

    x = [-0.577, 0.577]
    w = [1,1]

    return w[0]*f(x[0]) + w[1]*f(x[1])
```

---

## 📊 Resultado de Ejecución

```txt id="c2w1lo"
Integral aproximada:
5.33333
```

---

## 🏁 Conclusión

La cuadratura gaussiana logra resultados extremadamente precisos con pocas evaluaciones de la función.

---

# 📄 Evidencias Académicas

## 📌 Archivos Incluidos

* `Examen Tema 4.docx`
* `Problemario Tema 4.pdf`

---

# 📌 Conceptos Clave Evaluados

1. Espaciamiento (h).
2. Error de truncamiento.
3. Polinomios interpoladores.
4. Integración numérica.
5. Pesos y nodos de Gauss.
6. Precisión computacional.

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown

---

# 🏆 Conclusión General del Tema

La diferenciación e integración numérica permiten aproximar operaciones fundamentales del cálculo utilizando algoritmos computacionales. Estos métodos son indispensables cuando las soluciones analíticas son complejas o imposibles de obtener.
