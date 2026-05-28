# Tema 3: Métodos de Solución de Sistemas de Ecuaciones 

Este directorio contiene las implementaciones algorítmicas y la documentación matemática para resolver sistemas de ecuaciones lineales simultáneas del tipo $[A]\{x\} = \{B\}$. El objetivo de esta unidad es dominar tanto los métodos numéricos directos (exactos) como los iterativos (aproximados) para el manejo eficiente de matrices.

---

## 📂 Estructura del Directorio

El contenido de este tema se divide en dos enfoques de resolución matricial:

### 📁 Métodos Directos (Algoritmos de Cancelación):
* **`Eliminacion_Gaussiana`:** Método clásico que transforma la matriz de coeficientes en una matriz triangular superior mediante operaciones elementales de fila, para posteriormente hallar las incógnitas mediante sustitución hacia atrás.
* **`Gauss_Jordan`:** Una extensión de la eliminación gaussiana que continúa operando hasta transformar la matriz de coeficientes en una matriz identidad. Esto permite obtener la solución de las variables de forma directa en el vector de términos independientes, sin necesidad de sustitución regresiva.

### 📁 Métodos Iterativos (Algoritmos de Aproximación):
* **`Gauss_Jacobi`:** Método iterativo que descompone la matriz y calcula los nuevos valores de cada incógnita basándose únicamente en las aproximaciones del paso o iteración anterior.
* **`Gauss_Seidel`:** Una optimización directa del método de Jacobi. A diferencia de este, Gauss-Seidel utiliza inmediatamente los valores recién calculados de las variables dentro de la misma iteración actual, lo que acelera significativamente la velocidad de convergencia.

---

## 📄 Documentos y Evidencias Académicas

En la raíz de esta carpeta se incluyen los archivos de entrega y evaluación teórica/práctica:

* **`Problemarion Tema 3.pdf`:** Documento formal en formato PDF que contiene la resolución detallada de los sistemas lineales propuestos, la verificación manual de los algoritmos y el análisis del número de iteraciones requeridas.
* **`Examen Tema 3.docx`:** Documento de Word con el desarrollo de la evaluación correspondiente a los métodos directos e iterativos aplicados en esta unidad.

---

## 📌 Conceptos Clave Evaluados
1. **Diagonal Dominante:** Condición matemática crucial en la matriz de coeficientes ($|a_{ii}| > \sum |a_{ij}|$) para garantizar la convergencia segura de los métodos iterativos como Jacobi y Gauss-Seidel.
2. **Pivoteo Parcial:** Estrategia utilizada en los métodos directos para evitar la división entre cero o reducir los errores de redondeo causados por coeficientes extremadamente pequeños en la diagonal principal.
3. **Criterio de Convergencia:** Monitoreo del error relativo porcentual aproximado en cada variable entre iteraciones consecutivas para detener el
