# 📘 Tema 1: Introducción a los Métodos Numéricos

Este directorio contiene las actividades prácticas, simulaciones y evidencias correspondientes a la Unidad 1 de Métodos Numéricos. El propósito principal de este tema es comprender cómo las computadoras representan los números y cómo se generan los diferentes errores computacionales durante los cálculos matemáticos.

En esta unidad se analizan conceptos fundamentales relacionados con precisión, exactitud y limitaciones del hardware en operaciones numéricas.

---

# 🛠️ Catálogo de Conceptos y Simulaciones Desarrolladas

| Recurso                   | Descripción                                        |
| :------------------------ | :------------------------------------------------- |
| Acumulación de Errores    | Propagación de errores en iteraciones repetitivas. |
| Cancelación por Resta     | Pérdida de precisión al restar números cercanos.   |
| Comparación Directa       | Problemas al comparar números flotantes con `==`.  |
| Conversión Estrecha       | Pérdida de datos al convertir tipos numéricos.     |
| Desbordamiento (Overflow) | Resultados fuera del rango permitido.              |
| Error de Redondeo Binario | Limitaciones de representación binaria.            |
| NaN (Not a Number)        | Operaciones matemáticas indefinidas.               |
| Precisión IEEE 754        | Limitaciones del estándar flotante.                |

---

# 1. 🔹 Error Absoluto y Error Relativo

## 🎯 Objetivo

Comprender cómo medir la diferencia entre un valor real y un valor aproximado dentro de los cálculos numéricos.

---

## 📝 Descripción

Los errores son inevitables en computación debido a las limitaciones de almacenamiento y representación de datos. El error absoluto mide la diferencia directa entre valores, mientras que el error relativo indica qué tan grande es el error respecto al valor real.

---

## 🔢 Fórmulas Generales

Error absoluto:

```txt id="mxgq9o"
Ea = |Valor_Real - Valor_Aproximado|
```

Error relativo:

```txt id="m6e4y7"
Er = Ea / Valor_Real
```

Error porcentual:

```txt id="kg5z0w"
Error % = Er * 100
```

---

## 👣 Pasos del Algoritmo

1. Obtener el valor real.
2. Obtener el valor aproximado.
3. Calcular el error absoluto.
4. Calcular el error relativo.
5. Interpretar el porcentaje de error.

---

## 💻 Pseudocódigo

```txt id="5eh87f"
INICIO

Leer valor_real
Leer valor_aproximado

Ea = abs(valor_real - valor_aproximado)

Er = Ea / valor_real

Mostrar resultados

FIN
```

---

## 🐍 Código en Python

```python id="q3l2pq"
valor_real = 10
valor_aproximado = 9.8

Ea = abs(valor_real - valor_aproximado)

Er = Ea / valor_real

print("Error absoluto:", Ea)
print("Error relativo:", Er)
```

---

## 🏁 Conclusión

Los errores absoluto y relativo permiten evaluar la precisión de un cálculo numérico y determinar qué tan confiable es una aproximación.

---

# 2. 🔹 Error de Redondeo Binario

## 🎯 Objetivo

Analizar cómo algunos números decimales no pueden representarse exactamente en sistema binario.

---

## 📝 Descripción

Las computadoras almacenan los números utilizando representación binaria. Algunos valores decimales aparentemente simples, como `0.1`, generan pequeñas diferencias internas debido a su conversión binaria infinita.

---

## 🔢 Ejemplo de Representación

```txt id="c8syc4"
0.1 + 0.2 = 0.30000000000000004
```

---

## 👣 Pasos del Algoritmo

1. Definir números decimales.
2. Realizar operación.
3. Mostrar resultado.
4. Comparar con valor esperado.

---

## 🐍 Código en Python

```python id="r9g0g9"
a = 0.1
b = 0.2

resultado = a + b

print(resultado)
```

---

## 📊 Resultado de Ejecución

```txt id="z4okb2"
0.30000000000000004
```

---

## 🏁 Conclusión

La representación binaria provoca pequeñas pérdidas de precisión que pueden acumularse durante cálculos complejos.

---

# 3. 🔹 Cancelación por Resta

## 🎯 Objetivo

Demostrar la pérdida de cifras significativas al restar números muy cercanos.

---

## 📝 Descripción

Cuando dos números flotantes poseen valores similares, la resta entre ellos elimina gran parte de sus dígitos significativos, reduciendo considerablemente la precisión.

---

## 🔢 Ejemplo

```txt id="0v6r3z"
1.0000001 - 1.0000000
```

---

## 🐍 Código en Python

```python id="c9ybmn"
a = 1.0000001
b = 1.0000000

resultado = a - b

print(resultado)
```

---

## 📊 Resultado

```txt id="i9v77k"
1.0000000005838672e-07
```

---

## 🏁 Conclusión

La cancelación numérica representa uno de los principales problemas de precisión en métodos científicos.

---

# 4. 🔹 Comparación Directa de Flotantes

## 🎯 Objetivo

Comprender por qué no es recomendable comparar números flotantes utilizando `==`.

---

## 📝 Descripción

Debido a errores de representación binaria, dos números que deberían ser iguales pueden diferir ligeramente.

---

## 🔢 Comparación Correcta

```txt id="s1xkp6"
abs(a - b) < epsilon
```

---

## 🐍 Código en Python

```python id="ruwzsl"
a = 0.1 + 0.2
b = 0.3

epsilon = 1e-9

print(abs(a - b) < epsilon)
```

---

## 📊 Resultado

```txt id="qnm5e1"
True
```

---

## 🏁 Conclusión

El uso de tolerancias evita errores lógicos al trabajar con números de punto flotante.

---

# 5. 🔹 Desbordamiento (Overflow)

## 🎯 Objetivo

Observar qué sucede cuando una operación supera el límite máximo permitido por el tipo de dato.

---

## 📝 Descripción

Cuando el resultado de un cálculo excede la capacidad de almacenamiento del sistema, ocurre un desbordamiento.

---

## 🐍 Código en Python

```python id="p77v0v"
numero = 1e308

resultado = numero * 1000

print(resultado)
```

---

## 📊 Resultado

```txt id="u1n2jv"
inf
```

---

## 🏁 Conclusión

El overflow puede generar resultados infinitos o inválidos dentro de los cálculos numéricos.

---

# 📄 Evidencias Académicas

## 📌 Archivos Incluidos

* `Problemario Tema 1.pdf`
* `Captura_Examen_T1.png`

---

# 📌 Conceptos Clave Evaluados

1. Precisión y exactitud.
2. Error absoluto y relativo.
3. Cifras significativas.
4. Representación binaria.
5. Cancelación numérica.
6. Desbordamiento.
7. Incertidumbre computacional.

---

# 🚀 Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Git & GitHub
* Markdown

---

# 🏆 Conclusión General del Tema

La introducción a los métodos numéricos permite comprender las limitaciones reales de las computadoras al trabajar con cálculos matemáticos. Estos conceptos son fundamentales para desarrollar algoritmos más precisos, estables y confiables dentro de la ingeniería y las ciencias computacionales.
