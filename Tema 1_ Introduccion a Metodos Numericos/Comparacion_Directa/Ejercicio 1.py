# 3. Comparación Directa con ==
import math

a = 0.1 + 0.1 + 0.1
b = 0.3

print(f"Valor de a (0.1 * 3): {a:.17f}")
print(f"Valor de b:           {b:.17f}")

print("\n--- Comparación con == ---")
if a == b:
    print("Resultado: Son iguales")
else:
    print("Resultado: SON DIFERENTES (Error esperado)")

# Solución: usar math.isclose() o épsilon manual
epsilon = 1e-9
print(f"\nComparación con math.isclose():")
if math.isclose(a, b, rel_tol=epsilon):
    print("Resultado: Son iguales (dentro del margen de error)")
else:
    print("Resultado: Son diferentes")

if abs(a - b) < epsilon:
    print("Épsilon manual: Son iguales")
