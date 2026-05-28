# Tema 1: Introducción a los Métodos Numéricos 

Este directorio contiene las actividades prácticas, evidencias y simulaciones de código correspondientes a la **Unidad 1**. El enfoque principal de este bloque es comprender cómo las computadoras almacenan los números, las limitaciones del hardware y cómo se originan y propagan los diferentes tipos de errores en el cómputo numérico.

---

## 📂 Estructura del Directorio

El contenido de este tema se organiza en los siguientes módulos prácticos:

### 📁 Demostraciones de Errores Comunes en Cómputo:
* **`Acumulacion_Errores_Bucles`:** Análisis de cómo un pequeño error de redondeo o truncamiento se magnifica de forma crítica al repetir operaciones miles de veces dentro de un ciclo (`for`/`while`).
* **`Cancelacion_Resta`:** Demostración del fenómeno de "cancelación catastrófica", que ocurre al restar dos números flotantes casi idénticos, provocando una pérdida masiva de dígitos significativos.
* **`Comparacion_Directa`:** Ejemplos de por qué **nunca** se deben comparar números de punto flotante usando un operador de igualdad directa (`==`), y cómo solucionarlo mediante tolerancias (`epsilon`).
* **`Conversion_Estrecha`:** Impacto y pérdida de datos al realizar un casteo o conversión de un tipo de dato de mayor precisión a uno menor (por ejemplo, de `double` a `float`, o de punto flotante a `int`).
* **`Dersbordamiento_Overflow`:** Simulación de situaciones donde el resultado de una operación supera el límite máximo almacenable por el tipo de dato, resultando en valores infinitos (`Infinity`) o errores en tiempo de ejecución.
* **`Error_Redondeo_Binario`:** Demostración práctica de cómo fracciones decimales exactas (como `0.1`) no pueden representarse de forma exacta en el sistema binario, generando pequeñas discrepancias de precisión.
* **`NaN_Not_a_Number`:** Manejo e identificación de indeterminaciones matemáticas en programación (como divisiones `0/0` o raíces cuadradas de números negativos).
* **`Perdida_Presicion_IEEE754`:** Análisis profundo del estándar IEEE 754 y cómo la limitación de bits en la mantisa provoca que números extremadamente grandes o pequeños pierdan precisión al operar entre sí.

---

## 📄 Documentos y Evidencias Académicas

Además de los códigos de simulación, en la raíz de esta carpeta se incluyen:

* **`Problemario Tema 1 .pdf`:** Documento con la resolución formal de los ejercicios prácticos, cálculos de errores (absoluto, relativo, porcentual) y análisis iterativos asignados para esta unidad.
* **`Captura_Examen T1.png`:** Evidencia digital de la evaluación correspondiente a los conceptos teóricos y prácticos de la introducción a los métodos numéricos.

---

## ⚙️ Conceptos Clave Evaluados
1. **Precisión vs. Exactitud:** La cercanía de los valores calculados entre sí frente a la cercanía con el valor real.
2. **Cifras Significativas:** El número de dígitos que se usan con confianza en un cálculo.
3. **Incertidumbre y Sesgo:** Errores sistemáticos y aleatorios presentes en el modelado numérico.
