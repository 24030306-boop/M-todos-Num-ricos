# Tema 4: Diferenciación e Integración Numérica 📈 📐

Este directorio contiene el desarrollo de algoritmos y códigos de simulación enfocados en aproximar las dos operaciones fundamentales del cálculo: la derivada y la integral definida. Estos métodos son esenciales cuando se trabaja con funciones complejas conocidas solo a través de un conjunto de datos discretos o cuyas antiderivadas analíticas no se pueden calcular.

---

## 📂 Estructura del Directorio

El contenido de esta unidad está organizado cronológicamente en los siguientes métodos prácticos:

### 📁 Módulos de Cálculo Numérico:
* **`Metodo 1_ Regla de Diferenciacion...`:** Implementación de fórmulas de diferencias finitas (hacia adelante, hacia atrás y centradas) para aproximar la pendiente de una función en un punto utilizando límites discretos y series de Taylor.
* **`Metodo 2_ Metodo del Trapecio...`:** Código basado en la regla de Newton-Cotes que aproxima el área bajo la curva mediante segmentos de líneas rectas (trapecios), incluyendo su versión compuesta para dividir el intervalo en múltiples segmentos y reducir el error.
* **`Metodo 3_ Metodo de Simpson...`:** Implementación de las reglas de Simpson (1/3 y 3/8) que mejoran la precisión del trapecio al conectar los puntos discretos mediante parábolas o funciones cúbicas en lugar de líneas rectas.
* **`Metodo 4_ Cuadratura Gaussiana`:** Algoritmo avanzado de integración numérica de alta precisión que evalúa la función en puntos óptimos no equiespaciados asignándoles pesos matemáticos específicos, maximizando la exactitud con un menor número de evaluaciones.

---

## 📄 Evidencias Académicas

En la raíz de esta carpeta se incluye el documento de evaluación del bloque:

* **`Examen Tema 4.docx`:** Documento de Word que recopila el desarrollo conceptual, la solución manual y las pruebas de escritorio de los problemas correspondientes a derivadas e integrales numéricas evaluados en este tema.

---

## 📌 Conceptos Clave Evaluados
1. **Espaciamiento ($h$):** El tamaño del intervalo entre puntos. Se analiza cómo un valor de $h$ más pequeño reduce el error de truncamiento, pero puede incrementar el error de redondeo en la computadora.
2. **Grado del Polinomio:** El nivel de precisión que se alcanza según la técnica (lineal en el trapecio, cuadrático/cúbico en Simpson).
3. **Puntos y Pesos de Gauss:** El uso de raíces de polinomios de Legendre para lograr la máxima precisión matemática con integrales definidas.
