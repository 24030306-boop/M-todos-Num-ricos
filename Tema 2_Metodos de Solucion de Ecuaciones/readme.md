# Tema 2: Métodos de Solución de Ecuaciones 

Este directorio contiene las implementaciones algorítmicas y hojas de cálculo utilizadas para resolver ecuaciones algebraicas y trascendentes del tipo $f(x) = 0$. El objetivo de esta unidad es comprender y aplicar métodos iterativos (tanto cerrados como abiertos) para aproximar las raíces de una función con un margen de error controlado.

---

## 📂 Estructura del Directorio

El contenido de este tema se divide en métodos de intervalo (cerrados) y métodos abiertos:

### 📁 Métodos Cerrados (Basados en Intervalos):
* **`Metodo_Biseccion`:** Algoritmo que divide sistemáticamente a la mitad un intervalo $[a, b]$ donde se garantiza la existencia de una raíz (por el Teorema de Bolzano), repitiendo el proceso hasta cumplir con la tolerancia permitida.
* **`Metodo_Falsa_Posicion`:** También conocido como *Regula Falsi*. Optimiza el método de bisección uniendo los puntos de los extremos mediante una línea recta (secante), utilizando la intersección de esta línea con el eje $x$ como la nueva aproximación.

### 📁 Métodos Abiertos (Basados en Valores Iniciales):
* **`Metodo_Newton_Rapson`:** Uno de los algoritmos más eficientes y de rápida convergencia (cuadrática). Utiliza el valor de la función y su primera derivada  $f(x)$ para trazar rectas tangentes que se aproximan velozmente a la raíz real.
* **`Metodo_Secante`:** Una variante del método de Newton-Raphson diseñada para casos donde calcular la derivada analítica de la función es muy complejo o imposible. Aproxima la derivada utilizando una diferencia finita basada en dos puntos iniciales.

---

## 📊 Hojas de Cálculo y Evidencias Académicas

En la raíz de esta carpeta se encuentran los archivos de Excel automatizados con fórmulas iterativas para validar los cálculos manuales y de código:

* **`Problemario Tema 2.xlsx`:** Plantillas y tablas iterativas que muestran paso a paso el comportamiento de las aproximaciones, el cálculo del error aproximado porcentual ($|\varepsilon_a|$) y la convergencia de los problemas asignados en clase.
* **`Examen Tema 2.xlsx`:** Archivo con la resolución práctica y evidencias numéricas correspondientes a la evaluación de esta unidad.

---

## 📌 Conceptos Clave Evaluados
1. **Convergencia:** La velocidad y certeza con la que un método se acerca al valor real de la raíz.
2. **Criterio de Parada:** Condición basada en la tolerancia permitida o en el error relativo porcentual para detener las iteraciones de manera segura.
3. **Limitaciones:** Análisis de casos donde los métodos abiertos pueden divergir (como puntos de inflexión o derivadas cercanas a cero en Newton-Raphson).
