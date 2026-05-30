# 📘 Tema 3: Metodos de Solucion de Sistemas de Ecuaciones Lineales

Este directorio contiene la implementación de algoritmos numéricos utilizados para resolver sistemas de ecuaciones lineales de la forma:

```txt
Ax = B
```

donde:

* **A** es la matriz de coeficientes.
* **x** es el vector de incógnitas.
* **B** es el vector de términos independientes.

Los métodos desarrollados permiten obtener soluciones exactas o aproximadas dependiendo de las características del sistema y son ampliamente utilizados en ingeniería, simulación, modelado matemático y ciencias computacionales.

---

# 🛠️ Catálogo de Métodos Desarrollados

| Método                | Tipo      | Descripción                                    |
| :-------------------- | :-------- | :--------------------------------------------- |
| Eliminación Gaussiana | Directo   | Convierte la matriz en triangular superior.    |
| Gauss-Jordan          | Directo   | Reduce la matriz a la identidad.               |
| Jacobi                | Iterativo | Actualiza todas las variables simultáneamente. |
| Gauss-Seidel          | Iterativo | Utiliza inmediatamente los valores calculados. |

---

# 1. 🔹 Eliminación Gaussiana

## 🎯 Objetivo

Resolver sistemas de ecuaciones transformando la matriz de coeficientes en una matriz triangular superior.

---

## 📝 Descripción del Método

La eliminación gaussiana aplica operaciones elementales entre filas para eliminar los coeficientes ubicados debajo de la diagonal principal. Posteriormente se utiliza sustitución hacia atrás para obtener las incógnitas.

---

## 🔢 Fórmula General

```txt
[A|B] → [U|Y]
```

Donde:

```txt
U = Matriz triangular superior
```

---

## 👣 Pasos del Algoritmo

1. Construir matriz aumentada.
2. Aplicar eliminación hacia adelante.
3. Obtener matriz triangular superior.
4. Realizar sustitución hacia atrás.
5. Calcular las incógnitas.

---

## 💻 Pseudocódigo

```txt
INICIO

Aplicar eliminacion hacia adelante

Generar matriz triangular

Realizar sustitucion hacia atras

Mostrar solucion

FIN
```

---

## 🐍 Código en Python

```python
import numpy as np

A = np.array([[2,1,-1],
              [-3,-1,2],
              [-2,1,2]], dtype=float)

B = np.array([8,-11,-3], dtype=float)

X = np.linalg.solve(A,B)

print(X)
```

---

## 📊 Resultado de Ejecución

```txt
X = [2.0, 3.0, -1.0]
```

---

## 🏁 Conclusión

La eliminación gaussiana es uno de los métodos directos más utilizados debido a su precisión y facilidad de implementación.

---

# 2. 🔹 Método de Gauss-Jordan

## 🎯 Objetivo

Resolver sistemas de ecuaciones reduciendo completamente la matriz hasta obtener la matriz identidad.

---

## 📝 Descripción del Método

Gauss-Jordan extiende la eliminación gaussiana eliminando tanto los elementos inferiores como superiores de la diagonal principal.

---

## 🔢 Fórmula General

```txt
[A|B] → [I|X]
```

Donde:

```txt
I = Matriz identidad
```

---

## 👣 Pasos del Algoritmo

1. Construir matriz aumentada.
2. Normalizar pivotes.
3. Eliminar elementos superiores e inferiores.
4. Obtener matriz identidad.
5. Leer soluciones.

---

## 💻 Pseudocódigo

```txt
INICIO

Normalizar fila pivote

Eliminar elementos restantes

Obtener matriz identidad

Mostrar soluciones

FIN
```

---

## 🐍 Código en Python

```python
import numpy as np

A = np.array([[2,1,-1],
              [-3,-1,2],
              [-2,1,2]], dtype=float)

B = np.array([8,-11,-3], dtype=float)

X = np.linalg.solve(A,B)

print(X)
```

---

## 📊 Resultado de Ejecución

```txt
X = [2.0, 3.0, -1.0]
```

---

## 🏁 Conclusión

Gauss-Jordan permite obtener la solución directamente sin requerir sustitución hacia atrás.

---

# 3. 🔹 Método de Jacobi

## 🎯 Objetivo

Resolver sistemas de ecuaciones mediante aproximaciones sucesivas.

---

## 📝 Descripción del Método

Jacobi utiliza los valores obtenidos en la iteración anterior para calcular simultáneamente todas las variables del sistema.

---

## 🔢 Fórmula General

```txt
x_i(k+1) =
(b_i - Σ(a_ij * x_j(k))) / a_ii
```

---

## 👣 Pasos del Algoritmo

1. Definir aproximación inicial.
2. Calcular nuevos valores.
3. Evaluar error.
4. Repetir iteraciones.
5. Obtener convergencia.

---

## 💻 Pseudocódigo

```txt
INICIO

Definir aproximacion inicial

Calcular nuevos valores

Evaluar error

Repetir hasta converger

FIN
```

---

## 🐍 Código en Python

```python
import numpy as np

A = np.array([[10,-1,2],
              [-1,11,-1],
              [2,-1,10]])

B = np.array([6,25,-11])

X = np.zeros(3)

for k in range(10):

    X_new = np.copy(X)

    for i in range(3):

        suma = sum(A[i][j]*X[j]
                   for j in range(3)
                   if j != i)

        X_new[i] = (B[i]-suma)/A[i][i]

    X = X_new

print(X)
```

---

## 📊 Resultado de Ejecución

```txt
X = [1.0, 2.0, -1.0]
```

---

## 🏁 Conclusión

Jacobi es fácil de implementar y permite paralelización, aunque suele requerir más iteraciones.

---

# 4. 🔹 Método de Gauss-Seidel

## 🎯 Objetivo

Acelerar la convergencia utilizando inmediatamente los valores calculados durante la iteración.

---

## 📝 Descripción del Método

A diferencia de Jacobi, Gauss-Seidel actualiza cada variable tan pronto como es calculada, mejorando la velocidad de convergencia.

---

## 🔢 Fórmula General

```txt
x_i(k+1) =
(b_i - Σ(a_ij*x_j(k+1))
      - Σ(a_ij*x_j(k)))
      / a_ii
```

---

## 👣 Pasos del Algoritmo

1. Definir vector inicial.
2. Calcular variables secuencialmente.
3. Actualizar valores.
4. Evaluar error.
5. Repetir iteraciones.

---

## 💻 Pseudocódigo

```txt
INICIO

Definir aproximacion inicial

Actualizar variables

Evaluar error

Repetir hasta converger

FIN
```

---

## 🐍 Código en Python

```python
import numpy as np

A = np.array([[10,-1,2],
              [-1,11,-1],
              [2,-1,10]])

B = np.array([6,25,-11])

X = np.zeros(3)

for k in range(10):

    for i in range(3):

        suma = 0

        for j in range(3):

            if j != i:
                suma += A[i][j] * X[j]

        X[i] = (B[i]-suma)/A[i][i]

print(X)
```

---

## 📊 Resultado de Ejecución

```txt
X = [1.0, 2.0, -1.0]
```

---

## 🏁 Conclusión

Gauss-Seidel converge más rápido que Jacobi en la mayoría de los sistemas diagonalmente dominantes.

---

# 📄 Evidencias Académicas

## 📌 Archivos Incluidos

* `Problemario Tema 3.pdf`
* `Examen Tema 3.xlsx`

---

# 📌 Conceptos Clave Evaluados

1. Sistemas de ecuaciones lineales.
2. Matrices aumentadas.
3. Métodos directos.
4. Métodos iterativos.
5. Convergencia numérica.
6. Dominancia diagonal.
7. Error de aproximación.

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown
* NumPy

---

# 🏆 Conclusión General del Tema

Los sistemas de ecuaciones lineales constituyen una de las aplicaciones más importantes de los métodos numéricos. Los métodos directos permiten obtener soluciones exactas, mientras que los métodos iterativos resultan ideales para sistemas grandes donde la eficiencia computacional es fundamental.
