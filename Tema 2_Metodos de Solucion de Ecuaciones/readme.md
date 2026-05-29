# 📘 Tema 2: Métodos de Solución de Ecuaciones

Este directorio contiene las implementaciones algorítmicas, ejercicios y simulaciones desarrolladas para resolver ecuaciones algebraicas y trascendentes de la forma:

```txt id="i5f0r1"
f(x) = 0
```

El objetivo principal de esta unidad es aplicar métodos numéricos iterativos capaces de aproximar raíces reales con un margen de error controlado mediante diferentes estrategias de convergencia.

---

# 🛠️ Catálogo de Métodos Desarrollados

| Método                   | Tipo    | Descripción                                                |
| :----------------------- | :------ | :--------------------------------------------------------- |
| Método de Bisección      | Cerrado | Divide el intervalo en dos partes iguales sucesivamente.   |
| Método de Falsa Posición | Cerrado | Utiliza una secante entre extremos para aproximar la raíz. |
| Método de Newton-Raphson | Abierto | Usa derivadas para aproximarse rápidamente a la raíz.      |
| Método de la Secante     | Abierto | Aproxima derivadas usando diferencias finitas.             |

---

# 1. 🔹 Método de Bisección

## 🎯 Objetivo

Encontrar una raíz aproximada dentro de un intervalo donde exista cambio de signo.

---

## 📝 Descripción del Método

El método de bisección se basa en el Teorema de Bolzano. Si una función continua cambia de signo en un intervalo ([a,b]), entonces existe al menos una raíz dentro de dicho intervalo.

El algoritmo divide repetidamente el intervalo a la mitad hasta alcanzar la tolerancia deseada.

---

## 🔢 Fórmula General

```txt id="jlwm8m"
c = (a + b) / 2
```

---

## 👣 Pasos del Algoritmo

1. Definir intervalo inicial.
2. Verificar cambio de signo.
3. Calcular punto medio.
4. Evaluar función.
5. Actualizar intervalo.
6. Repetir iteraciones.

---

## 💻 Pseudocódigo

```txt id="n9p1l4"
INICIO

Leer a,b

Mientras error > tolerancia

   c = (a+b)/2

   Si f(a)*f(c) < 0
      b = c
   Sino
      a = c

Fin Mientras

Mostrar c

FIN
```

---

## 🐍 Código en Python

```python id="6rl2nr"
def biseccion(f, a, b, tol):

    while abs(b - a) > tol:

        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c
```

---

## 📊 Resultado de Ejecución

```txt id="l5g5gq"
Raíz aproximada:
x = 2.00001
```

---

## 🏁 Conclusión

Es un método seguro y estable, aunque suele requerir muchas iteraciones para converger.

---

# 2. 🔹 Método de Falsa Posición

## 🎯 Objetivo

Acelerar la convergencia utilizando una aproximación lineal entre los extremos del intervalo.

---

## 📝 Descripción del Método

El método de falsa posición utiliza una línea secante entre los extremos del intervalo para calcular una mejor aproximación de la raíz.

---

## 🔢 Fórmula General

```txt id="rx2u1g"
c = b - (f(b)*(a-b)) / (f(a)-f(b))
```

---

## 👣 Pasos del Algoritmo

1. Seleccionar intervalo inicial.
2. Construir secante.
3. Calcular intersección con eje x.
4. Actualizar intervalo.
5. Repetir iteraciones.

---

## 💻 Pseudocódigo

```txt id="c4f6te"
INICIO

Leer a,b

Mientras error > tolerancia

   c = b - (f(b)*(a-b))/(f(a)-f(b))

   Actualizar intervalo

Fin Mientras

Mostrar c

FIN
```

---

## 🐍 Código en Python

```python id="n0h0lq"
def falsa_posicion(f, a, b, tol):

    while abs(b - a) > tol:

        c = b - (f(b)*(a-b)) / (f(a)-f(b))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c
```

---

## 📊 Resultado de Ejecución

```txt id="g8nl7w"
Raíz aproximada:
x = 1.99999
```

---

## 🏁 Conclusión

La falsa posición suele converger más rápido que bisección al utilizar interpolación lineal.

---

# 3. 🔹 Método de Newton-Raphson

## 🎯 Objetivo

Encontrar raíces mediante aproximaciones sucesivas usando derivadas.

---

## 📝 Descripción del Método

Newton-Raphson es uno de los métodos más rápidos para encontrar raíces. Utiliza la recta tangente de la función para aproximar el siguiente valor.

---

## 🔢 Fórmula General

```txt id="o4b0h9"
x(n+1) = x(n) - f(x(n)) / f'(x(n))
```

---

## 👣 Pasos del Algoritmo

1. Elegir valor inicial.
2. Evaluar función y derivada.
3. Calcular nueva aproximación.
4. Verificar error.
5. Repetir proceso.

---

## 💻 Pseudocódigo

```txt id="t2r4oe"
INICIO

Leer x0

Mientras error > tolerancia

   x1 = x0 - f(x0)/f'(x0)

   x0 = x1

Fin Mientras

Mostrar x1

FIN
```

---

## 🐍 Código en Python

```python id="p0m6j2"
def newton_raphson(f, df, x0, tol):

    while True:

        x1 = x0 - f(x0)/df(x0)

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1
```

---

## 📊 Resultado de Ejecución

```txt id="d8hhpa"
Raíz aproximada:
x = 2.000000
```

---

## 🏁 Conclusión

Newton-Raphson posee convergencia rápida, aunque depende de una buena aproximación inicial.

---

# 4. 🔹 Método de la Secante

## 🎯 Objetivo

Resolver ecuaciones sin necesidad de calcular derivadas analíticas.

---

## 📝 Descripción del Método

El método de la secante aproxima la derivada usando dos valores iniciales y una recta secante entre ellos.

---

## 🔢 Fórmula General

```txt id="v7iv7m"
x(n+1) =
x(n) - [f(x(n))*(x(n)-x(n-1))] /
[f(x(n))-f(x(n-1))]
```

---

## 👣 Pasos del Algoritmo

1. Elegir dos valores iniciales.
2. Calcular aproximación.
3. Actualizar valores.
4. Verificar error.
5. Repetir iteraciones.

---

## 💻 Pseudocódigo

```txt id="w9tx4d"
INICIO

Leer x0,x1

Mientras error > tolerancia

   x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))

   x0 = x1
   x1 = x2

Fin Mientras

Mostrar x2

FIN
```

---

## 🐍 Código en Python

```python id="wq2q4k"
def secante(f, x0, x1, tol):

    while abs(x1 - x0) > tol:

        x2 = x1 - (f(x1)*(x1-x0)) / (f(x1)-f(x0))

        x0 = x1
        x1 = x2

    return x2
```

---

## 📊 Resultado de Ejecución

```txt id="y2w8l4"
Raíz aproximada:
x = 2.000000
```

---

## 🏁 Conclusión

El método de la secante ofrece buena velocidad de convergencia sin requerir derivadas explícitas.

---

# 📄 Evidencias Académicas

## 📌 Archivos Incluidos

* `Problemario Tema 2.xlsx`
* `Examen Tema 2.xlsx`

---

# 📌 Conceptos Clave Evaluados

1. Convergencia numérica.
2. Error relativo porcentual.
3. Tolerancia y criterio de parada.
4. Métodos cerrados y abiertos.
5. Estabilidad numérica.
6. Divergencia de algoritmos iterativos.

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown
* Microsoft Excel

---

# 🏆 Conclusión General del Tema

Los métodos de solución de ecuaciones permiten aproximar raíces de funciones matemáticas mediante algoritmos iterativos. La elección del método depende de factores como velocidad de convergencia, estabilidad y disponibilidad de derivadas analíticas.
