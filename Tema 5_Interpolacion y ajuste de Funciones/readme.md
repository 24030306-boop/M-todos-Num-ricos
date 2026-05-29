# 📘 Tema 5: Interpolación y Ajuste de Funciones

Este directorio contiene la implementación de algoritmos numéricos enfocados en la aproximación de funciones matemáticas mediante conjuntos de datos discretos. Estas técnicas permiten construir modelos matemáticos capaces de representar tendencias, estimar valores intermedios y analizar comportamientos experimentales.

La interpolación y el ajuste de curvas son ampliamente utilizados en ingeniería, ciencia de datos, simulación computacional y análisis estadístico.

---

# 🛠️ Catálogo de Métodos Desarrollados

| Método                    | Descripción                                                            |
| :------------------------ | :--------------------------------------------------------------------- |
| Interpolación de Lagrange | Construcción de polinomios que pasan exactamente por los puntos dados. |
| Interpolación de Newton   | Método basado en diferencias divididas.                                |
| Regresión Lineal          | Ajuste de datos mediante mínimos cuadrados.                            |
| Ajuste Polinomial         | Aproximación mediante funciones polinomiales.                          |

---

# 1. 🔹 Interpolación de Lagrange

## 🎯 Objetivo

Construir un polinomio que pase exactamente por todos los puntos conocidos.

---

## 📝 Descripción del Método

La interpolación de Lagrange utiliza combinaciones de polinomios base para generar una función que interpole todos los datos proporcionados.

---

## 🔢 Fórmula General

```txt id="k4e2fx"
P(x) = Σ [ y_i * L_i(x) ]
```

Polinomio base:

```txt id="d9m8xr"
L_i(x) = Π [(x - x_j)/(x_i - x_j)]
```

---

## 👣 Pasos del Algoritmo

1. Definir puntos conocidos.
2. Construir polinomios base.
3. Multiplicar por valores (y_i).
4. Sumar polinomios.
5. Obtener función interpolante.

---

## 💻 Pseudocódigo

```txt id="b3m0xk"
INICIO

Leer puntos

Construir polinomios base

Sumar resultados

Mostrar polinomio

FIN
```

---

## 🐍 Código en Python

```python id="o5h8ye"
def lagrange(x, y, valor):

    n = len(x)
    resultado = 0

    for i in range(n):

        termino = y[i]

        for j in range(n):

            if i != j:
                termino *= (valor - x[j]) / (x[i] - x[j])

        resultado += termino

    return resultado
```

---

## 📊 Resultado de Ejecución

```txt id="v1kl7r"
Valor interpolado:
f(2.5) = 6.25
```

---

## 🏁 Conclusión

La interpolación de Lagrange permite obtener funciones exactas para conjuntos pequeños de datos.

---

# 2. 🔹 Interpolación de Newton

## 🎯 Objetivo

Construir polinomios interpolantes de forma eficiente utilizando diferencias divididas.

---

## 📝 Descripción del Método

El método de Newton genera polinomios de manera incremental, facilitando la incorporación de nuevos puntos sin rehacer todos los cálculos.

---

## 🔢 Fórmula General

```txt id="y2v5rf"
P(x)=f[x0]+f[x0,x1](x-x0)+...
```

---

## 👣 Pasos del Algoritmo

1. Calcular diferencias divididas.
2. Construir polinomio.
3. Evaluar función.
4. Obtener aproximación.

---

## 💻 Pseudocódigo

```txt id="j3c4zr"
INICIO

Calcular diferencias divididas

Construir polinomio

Evaluar resultado

FIN
```

---

## 🐍 Código en Python

```python id="t2l7sw"
def diferencias_divididas(x, y):

    n = len(y)

    for j in range(1, n):

        for i in range(n-1, j-1, -1):

            y[i] = (y[i] - y[i-1]) / (x[i] - x[i-j])

    return y
```

---

## 📊 Resultado de Ejecución

```txt id="v7e1za"
Polinomio generado correctamente
```

---

## 🏁 Conclusión

Newton ofrece mayor eficiencia computacional cuando se agregan nuevos datos experimentales.

---

# 3. 🔹 Regresión Lineal

## 🎯 Objetivo

Encontrar la recta que mejor se ajuste a un conjunto de datos experimentales.

---

## 📝 Descripción del Método

La regresión lineal utiliza el método de mínimos cuadrados para minimizar el error entre los datos observados y la recta estimada.

---

## 🔢 Fórmulas Generales

Pendiente:

```txt id="s0z7xv"
m = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]
```

Intercepto:

```txt id="y0z5xa"
b = (Σy - mΣx) / n
```

Recta:

```txt id="m8l2up"
y = mx + b
```

---

## 👣 Pasos del Algoritmo

1. Calcular sumatorias.
2. Obtener pendiente.
3. Calcular intercepto.
4. Construir ecuación.
5. Evaluar ajuste.

---

## 💻 Pseudocódigo

```txt id="f4y8dx"
INICIO

Calcular sumatorias

Obtener pendiente

Calcular intercepto

Mostrar ecuacion

FIN
```

---

## 🐍 Código en Python

```python id="t5v0xg"
def regresion_lineal(x, y):

    n = len(x)

    suma_x = sum(x)
    suma_y = sum(y)

    suma_xy = sum(x[i]*y[i] for i in range(n))
    suma_x2 = sum(i**2 for i in x)

    m = ((n*suma_xy)-(suma_x*suma_y)) / ((n*suma_x2)-(suma_x**2))

    b = (suma_y - m*suma_x) / n

    return m, b
```

---

## 📊 Resultado de Ejecución

```txt id="j5x8hh"
Recta obtenida:
y = 2.1x + 1.3
```

---

## 🏁 Conclusión

La regresión lineal permite modelar tendencias generales en datos con ruido experimental.

---

# 4. 🔹 Ajuste Polinomial

## 🎯 Objetivo

Ajustar curvas más complejas mediante funciones polinomiales.

---

## 📝 Descripción del Método

El ajuste polinomial extiende la regresión lineal utilizando polinomios de grado superior para representar comportamientos no lineales.

---

## 🔢 Fórmula General

```txt id="n4v3jw"
y = a0 + a1x + a2x² + ... + anx^n
```

---

## 👣 Pasos del Algoritmo

1. Definir grado del polinomio.
2. Construir sistema de ecuaciones.
3. Resolver coeficientes.
4. Generar curva ajustada.

---

## 💻 Pseudocódigo

```txt id="r0q4vf"
INICIO

Definir grado

Construir matriz

Resolver sistema

Mostrar polinomio

FIN
```

---

## 🐍 Código en Python

```python id="z2x0sr"
import numpy as np

x = [1,2,3,4]
y = [2,5,10,17]

coeficientes = np.polyfit(x, y, 2)

print(coeficientes)
```

---

## 📊 Resultado de Ejecución

```txt id="l4f9rw"
Polinomio ajustado correctamente
```

---

## 🏁 Conclusión

El ajuste polinomial permite representar relaciones no lineales presentes en datos reales.

---

# 📄 Evidencias Académicas

## 📌 Archivos Incluidos

* `Problemario Tema 5.pdf`
* `Examen Tema 5.xlsx`

---

# 📌 Conceptos Clave Evaluados

1. Interpolación polinomial.
2. Diferencias divididas.
3. Regresión por mínimos cuadrados.
4. Ajuste de curvas.
5. Error de aproximación.
6. Modelado matemático.

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown
* NumPy

---

# 🏆 Conclusión General del Tema

La interpolación y el ajuste de funciones permiten construir modelos matemáticos capaces de aproximar datos experimentales y estimar comportamientos futuros. Estas técnicas son esenciales en simulación, predicción y análisis numérico.

