# 4. Acumulación de Errores en Bucles
from decimal import Decimal

iteraciones = 1_000_000
incremento  = 0.1

suma_float = 0.0
for _ in range(iteraciones):
    suma_float += incremento

esperado = iteraciones * incremento

print("--- Acumulación en Bucle (1,000,000 iteraciones) ---")
print(f"Resultado esperado: {esperado:.17f}")
print(f"Resultado float:    {suma_float:.17f}")
print(f"Diferencia (Error): {suma_float - esperado:.17f}")

# Solución con Decimal
suma_decimal = Decimal("0")
inc_decimal  = Decimal("0.1")
for _ in range(iteraciones):
    suma_decimal += inc_decimal

print("\n--- Solución con Decimal ---")
print(f"Resultado exacto: {suma_decimal}")

if suma_float != esperado:
    print("\nNOTA: El error de float es notable tras un millón de sumas.")
