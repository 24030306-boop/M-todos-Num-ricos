# 📈 Tema 6: Solución Numérica de Ecuaciones Diferenciales

Este módulo comprende el análisis, diseño e implementación de algoritmos numéricos utilizados para resolver Problemas de Valor Inicial (PVI) asociados a Ecuaciones Diferenciales Ordinarias (EDO). Estas técnicas permiten aproximar soluciones matemáticas cuando obtener una solución analítica exacta resulta difícil o imposible.

Las ecuaciones diferenciales son fundamentales en áreas como ingeniería, física, electrónica, simulación y modelado de fenómenos dinámicos.

---

# 🛠️ Catálogo de Métodos Desarrollados

| Método                                   | Descripción                                                                      |
| :--------------------------------------- | :------------------------------------------------------------------------------- |
| Método de Euler                          | Aproximación lineal básica utilizando la pendiente inicial del intervalo.        |
| Método de Euler Modificado (Heun)        | Mejora la precisión usando predicción y corrección mediante pendientes promedio. |
| Método de Runge-Kutta de 4to Orden (RK4) | Método de alta precisión basado en cuatro pendientes ponderadas.                 |

---

# 1. 🔹 Método de Euler

## 🎯 Objetivo

Aproximar la solución de una ecuación diferencial utilizando incrementos pequeños y pendientes lineales calculadas en el inicio de cada intervalo.

---

## 📝 Descripción del Método

El método de Euler es uno de los algoritmos numéricos más simples para resolver ecuaciones diferenciales ordinarias. Consiste en avanzar paso a paso utilizando la pendiente de la función en el punto actual para estimar el siguiente valor.

---

## 🔢 Fórmula General

[
y_{i+1}=y_i+h\cdot f(x_i,y_i)
]

Donde:

* (h) = tamaño del paso
* (f(x_i,y_i)) = pendiente de la función
* (y_{i+1}) = siguiente aproximación

---

## 👣 Pasos del Algoritmo

1. Definir la ecuación diferencial.
2. Establecer condición inicial.
3. Definir tamaño del paso.
4. Calcular pendiente.
5. Actualizar valor de (y).
6. Repetir hasta llegar al intervalo deseado.

---

## 💻 Pseudocódigo

```txt id="g2kq1v"
INICIO

Leer x0, y0, h

Mientras x <= xFinal

   y = y + h*f(x,y)

   x = x + h

Fin Mientras

FIN
```

---

## 🐍 Código en Python

```python id="x1m4pw"
def metodo_euler(f, x0, y0, h, x_final):

    x = x0
    y = y0

    while x <= x_final:

        print(f"x = {x:.2f}, y = {y:.5f}")

        y = y + h * f(x, y)

        x += h
```

---

## 📊 Resultado de Ejecución

```txt id="tfm0ls"
x = 0.00, y = 1.00000
x = 0.10, y = 1.10000
x = 0.20, y = 1.22000
x = 0.30, y = 1.36200
```

---

## 🏁 Conclusión

El método de Euler es sencillo y fácil de implementar, aunque presenta errores acumulativos significativos cuando el tamaño del paso es grande.

---

# 2. 🔹 Método de Euler Modificado (Heun)

## 🎯 Objetivo

Reducir el error de aproximación del método de Euler utilizando una corrección basada en el promedio de pendientes.

---

## 📝 Descripción del Método

El método de Heun mejora la aproximación obtenida por Euler utilizando dos pendientes:

* pendiente inicial
* pendiente estimada al final del intervalo

Posteriormente ambas pendientes se promedian para obtener una aproximación más precisa.

---

## 🔢 Fórmulas Generales

Predicción:

[
y_{i+1}^{*}=y_i+h\cdot f(x_i,y_i)
]

Corrección:

[
y_{i+1}=y_i+\frac{h}{2}[f(x_i,y_i)+f(x_{i+1},y_{i+1}^{*})]
]

---

## 👣 Pasos del Algoritmo

1. Calcular pendiente inicial.
2. Predecir nuevo valor.
3. Calcular pendiente final.
4. Promediar pendientes.
5. Actualizar solución.

---

## 💻 Pseudocódigo

```txt id="rj2z0f"
INICIO

Calcular pendiente inicial

Predecir y*

Calcular pendiente final

Corregir valor de y

Repetir iteraciones

FIN
```

---

## 🐍 Código en Python

```python id="s6bh4y"
def metodo_heun(f, x0, y0, h, x_final):

    x = x0
    y = y0

    while x <= x_final:

        print(f"x = {x:.2f}, y = {y:.5f}")

        pendiente_inicial = f(x, y)

        y_pred = y + h * pendiente_inicial

        pendiente_final = f(x + h, y_pred)

        y = y + (h / 2) * (pendiente_inicial + pendiente_final)

        x += h
```

---

## 📊 Resultado de Ejecución

```txt id="zw5ykt"
x = 0.00, y = 1.00000
x = 0.10, y = 1.11000
x = 0.20, y = 1.24205
x = 0.30, y = 1.39847
```

---

## 🏁 Conclusión

Euler Modificado ofrece mayor precisión que Euler simple sin incrementar demasiado el costo computacional.

---

# 3. 🔹 Método de Runge-Kutta de 4to Orden (RK4)

## 🎯 Objetivo

Obtener soluciones numéricas altamente precisas mediante el promedio ponderado de cuatro pendientes evaluadas en distintos puntos del intervalo.

---

## 📝 Descripción del Método

RK4 es uno de los métodos más utilizados para resolver ecuaciones diferenciales debido a su gran precisión y estabilidad numérica. Utiliza cuatro evaluaciones de pendiente en cada iteración.

---

## 🔢 Fórmulas Generales

[
k_1=f(x_i,y_i)
]

[
k_2=f\left(x_i+\frac{h}{2},y_i+\frac{h k_1}{2}\right)
]

[
k_3=f\left(x_i+\frac{h}{2},y_i+\frac{h k_2}{2}\right)
]

[
k_4=f(x_i+h,y_i+h k_3)
]

Actualización:

[
y_{i+1}=y_i+\frac{h}{6}(k_1+2k_2+2k_3+k_4)
]

---

## 👣 Pasos del Algoritmo

1. Calcular (k_1)
2. Calcular (k_2)
3. Calcular (k_3)
4. Calcular (k_4)
5. Obtener promedio ponderado.
6. Actualizar solución.

---

## 💻 Pseudocódigo

```txt id="3z7xkp"
INICIO

Calcular k1
Calcular k2
Calcular k3
Calcular k4

Actualizar y

Repetir proceso

FIN
```

---

## 🐍 Código en Python

```python id="i1pkqo"
def metodo_rk4(f, x0, y0, h, x_final):

    x = x0
    y = y0

    while x <= x_final:

        print(f"x = {x:.2f}, y = {y:.6f}")

        k1 = f(x, y)

        k2 = f(x + h/2, y + (h*k1)/2)

        k3 = f(x + h/2, y + (h*k2)/2)

        k4 = f(x + h, y + h*k3)

        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        x += h
```

---

## 📊 Resultado de Ejecución

```txt id="6w74aq"
x = 0.00, y = 1.000000
x = 0.10, y = 1.110342
x = 0.20, y = 1.242805
x = 0.30, y = 1.399717
```

---

## 🏁 Conclusión

Runge-Kutta de cuarto orden proporciona resultados muy precisos y estables, siendo uno de los métodos más utilizados en simulación numérica e ingeniería.

---

# 📌 Comparación General de Métodos

| Método           | Precisión | Velocidad | Complejidad |
| :--------------- | :-------: | :-------: | :---------: |
| Euler            |    Baja   |    Alta   |     Baja    |
| Euler Modificado |   Media   |   Media   |    Media    |
| RK4              |  Muy Alta |   Menor   |     Alta    |

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown

---

# 🏆 Conclusión General del Tema

Los métodos numéricos para ecuaciones diferenciales permiten modelar fenómenos reales mediante aproximaciones computacionales. Conforme aumenta la complejidad del método, también mejora la precisión de los resultados obtenidos. RK4 destaca por ofrecer una excelente relación entre estabilidad y exactitud numérica.

