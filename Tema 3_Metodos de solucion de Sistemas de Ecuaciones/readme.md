# 📊 TEMA 3: Sistemas de Ecuaciones Lineales

Implementación de algoritmos numéricos para resolver sistemas de ecuaciones lineales de la forma:

A\vec{x}=\vec{b}

En este tema se desarrollan métodos directos e iterativos utilizados para encontrar soluciones aproximadas o exactas de sistemas lineales. También se realiza un análisis comparativo respecto a eficiencia, convergencia y estabilidad numérica.

---

# 🔍 Métodos Incluidos

## 📌 Métodos Directos

🔹 Eliminación Gaussiana
🔹 Método de Gauss-Jordan

## 📌 Métodos Iterativos

🔸 Método de Jacobi
🔸 Método de Gauss-Seidel

---

# 🛠️ Catálogo de Métodos Desarrollados

# 1. 🔹 Eliminación Gaussiana

## 🎯 Objetivo

Transformar un sistema de ecuaciones lineales en una matriz triangular superior para resolverlo mediante sustitución hacia atrás.

---

## 📝 Descripción del Método

La eliminación gaussiana utiliza operaciones elementales entre filas para convertir la matriz aumentada en una matriz triangular superior. Posteriormente se despejan las incógnitas comenzando desde la última ecuación.

---

## 🔢 Fórmula General

Transformación:

[
[A|B] \rightarrow [U|Y]
]

donde:

* (A) = matriz de coeficientes
* (B) = vector de términos independientes
* (U) = matriz triangular superior

---

## 👣 Pasos del Algoritmo

1. Construir la matriz aumentada.
2. Aplicar eliminación hacia adelante.
3. Generar ceros debajo de la diagonal principal.
4. Aplicar sustitución hacia atrás.
5. Obtener el vector solución.

---

## 💻 Pseudocódigo

```txt id="g2n5fx"
INICIO

Para i <- 0 Hasta n-1

   Para j <- i+1 Hasta n-1

      factor <- A[j][i] / A[i][i]

      Para k <- i Hasta n-1
         A[j][k] <- A[j][k] - factor*A[i][k]
      Fin Para

      B[j] <- B[j] - factor*B[i]

   Fin Para

Fin Para

Aplicar sustitución hacia atrás

FIN
```

---

## 🐍 Código en Python

```python id="6n2d4x"
def eliminacion_gaussiana(A, B):
    n = len(B)

    for i in range(n):
        for j in range(i + 1, n):

            factor = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

            B[j] -= factor * B[i]

    X = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):

        suma = 0

        for j in range(i + 1, n):
            suma += A[i][j] * X[j]

        X[i] = (B[i] - suma) / A[i][i]

    return X
```

---

## 📊 Resultado de Ejecución

```txt id="ovvyn5"
Sistema resuelto correctamente.

Solución:
X0 = 1.0
X1 = -2.0
X2 = 3.0
```

---

## 🏁 Conclusión

La eliminación gaussiana es un método eficiente y exacto para sistemas pequeños y medianos. Sin embargo, puede presentar errores numéricos si no se implementa pivoteo.

---

# 2. 🔹 Método de Gauss-Jordan

## 🎯 Objetivo

Reducir la matriz de coeficientes hasta convertirla en una matriz identidad para obtener directamente la solución del sistema.

---

## 📝 Descripción del Método

Gauss-Jordan extiende la eliminación gaussiana eliminando tanto arriba como debajo de cada pivote, normalizando además cada fila pivote.

---

## 🔢 Fórmula General

[
[A|B] \rightarrow [I|X]
]

donde:

* (I) = matriz identidad
* (X) = vector solución

---

## 👣 Pasos del Algoritmo

1. Seleccionar pivote.
2. Normalizar fila pivote.
3. Hacer ceros arriba y abajo del pivote.
4. Repetir para todas las columnas.
5. Obtener solución directa.

---

## 💻 Pseudocódigo

```txt id="ps5flw"
INICIO

Para i <- 0 Hasta n-1

   pivote <- A[i][i]

   Normalizar fila pivote

   Para j <- 0 Hasta n-1

      Si j != i

         Eliminar elementos

      Fin Si

   Fin Para

Fin Para

FIN
```

---

## 🐍 Código en Python

```python id="5y3bzw"
def gauss_jordan(A, B):

    n = len(B)

    for i in range(n):

        pivote = A[i][i]

        for k in range(n):
            A[i][k] /= pivote

        B[i] /= pivote

        for j in range(n):

            if j != i:

                factor = A[j][i]

                for k in range(n):
                    A[j][k] -= factor * A[i][k]

                B[j] -= factor * B[i]

    return B
```

---

## 📊 Resultado de Ejecución

```txt id="4vmyaj"
Matriz reducida correctamente.

Solución:
[1.0, -2.0, 3.0]
```

---

## 🏁 Conclusión

Gauss-Jordan permite obtener directamente el vector solución, aunque requiere mayor cantidad de operaciones.

---

# 3. 🔸 Método de Jacobi

## 🎯 Objetivo

Resolver sistemas lineales mediante aproximaciones sucesivas usando iteraciones independientes.

---

## 📝 Descripción del Método

Jacobi utiliza únicamente los valores de la iteración anterior para calcular las nuevas aproximaciones.

---

## 🔢 Fórmula General

x_i^{(k+1)}=\frac{b_i-\sum_{j\neq i}a_{ij}x_j^{(k)}}{a_{ii}}

---

## 👣 Pasos del Algoritmo

1. Inicializar vector solución.
2. Aplicar fórmula iterativa.
3. Calcular error.
4. Verificar convergencia.
5. Repetir hasta cumplir tolerancia.

---

## 🐍 Código en Python

```python id="fpkkt2"
def jacobi(A, B, X, tol, max_iter):

    n = len(B)

    for _ in range(max_iter):

        X_nuevo = X.copy()

        for i in range(n):

            suma = 0

            for j in range(n):

                if j != i:
                    suma += A[i][j] * X[j]

            X_nuevo[i] = (B[i] - suma) / A[i][i]

        error = max(abs(X_nuevo[i] - X[i]) for i in range(n))

        if error < tol:
            return X_nuevo

        X = X_nuevo.copy()

    return X
```

---

## 📊 Resultado de Ejecución

```txt id="8mncdz"
Iteraciones: 18

Solución aproximada:
[0.99999, -1.99998, 3.00001]
```

---

## 🏁 Conclusión

Jacobi es sencillo de implementar y puede paralelizarse fácilmente, aunque suele requerir muchas iteraciones.

---

# 4. 🔸 Método de Gauss-Seidel

## 🎯 Objetivo

Acelerar la convergencia utilizando inmediatamente los nuevos valores calculados en cada iteración.

---

## 📝 Descripción del Método

Gauss-Seidel mejora el método de Jacobi utilizando las aproximaciones recién calculadas durante la misma iteración.

---

## 🔢 Fórmula General

x_i^{(k+1)}=\frac{b_i-\sum_{j<i}a_{ij}x_j^{(k+1)}-\sum_{j>i}a_{ij}x_j^{(k)}}{a_{ii}}

---

## 👣 Pasos del Algoritmo

1. Inicializar solución.
2. Actualizar valores inmediatamente.
3. Calcular error.
4. Repetir iteraciones.
5. Verificar convergencia.

---

## 🐍 Código en Python

```python id="y7a0h6"
def gauss_seidel(A, B, X, tol, max_iter):

    n = len(B)

    for _ in range(max_iter):

        error = 0

        for i in range(n):

            suma = 0

            for j in range(n):

                if j != i:
                    suma += A[i][j] * X[j]

            nuevo = (B[i] - suma) / A[i][i]

            error = max(error, abs(nuevo - X[i]))

            X[i] = nuevo

        if error < tol:
            return X

    return X
```

---

## 📊 Resultado de Ejecución

```txt id="l6r0rk"
Iteraciones: 9

Solución aproximada:
[1.00000, -2.00000, 3.00000]
```

---

## 🏁 Conclusión

Gauss-Seidel converge más rápido que Jacobi en la mayoría de los casos y requiere menos iteraciones.

---

# 📌 Comparación General de Métodos

| Método                | Tipo      | Ventaja          | Desventaja                |
| --------------------- | --------- | ---------------- | ------------------------- |
| Eliminación Gaussiana | Directo   | Exactitud alta   | Mayor costo computacional |
| Gauss-Jordan          | Directo   | Solución directa | Más operaciones           |
| Jacobi                | Iterativo | Paralelizable    | Convergencia lenta        |
| Gauss-Seidel          | Iterativo | Más rápido       | Dependencia secuencial    |

---

# 🏆 Conclusión General del Tema

Los métodos para resolver sistemas de ecuaciones lineales son fundamentales dentro de los métodos numéricos. Los métodos directos proporcionan soluciones exactas con mayor costo computacional, mientras que los métodos iterativos son ideales para sistemas grandes debido a su eficiencia y menor uso de memoria.
