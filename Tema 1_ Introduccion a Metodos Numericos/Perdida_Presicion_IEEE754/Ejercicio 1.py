# 2. Pérdida de Precisión por Magnitud (IEEE 754)
from decimal import Decimal

numero_grande  = 1.0e16
numero_pequeno = 1.0
resultado      = numero_grande + numero_pequeno

print("--- Demostración de Pérdida de Precisión ---")
print(f"Número Grande:   {numero_grande}")
print(f"Número Pequeño:  {numero_pequeno}")
print(f"Suma Resultante: {resultado}")

if resultado == numero_grande:
    print("\nRESULTADO: El número pequeño 'desapareció'.")
    print("La suma es igual al número original por falta de bits.")

# Solución con Decimal (equivalente a BigDecimal en Java)
print("\n--- Solución con Decimal ---")
bd_grande  = Decimal("1e16")
bd_pequeno = Decimal("1")
bd_resultado = bd_grande + bd_pequeno
print(f"Suma Exacta: {bd_resultado}")
