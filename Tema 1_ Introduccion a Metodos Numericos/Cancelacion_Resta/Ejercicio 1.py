# 5. Cancelación por Resta (Loss of Significance)
from decimal import Decimal, getcontext

x = 1234567890.1234567
y = 1234567890.1234560

resultado = x - y

print(f"x = {x:.20f}")
print(f"y = {y:.20f}")
print(f"Resultado real (float): {resultado:.20f}")
print(f"Resultado esperado:     0.0000007")

# Solución con Decimal de alta precisión
getcontext().prec = 30
dx = Decimal("1234567890.1234567")
dy = Decimal("1234567890.1234560")
print(f"\nSolución Decimal: {dx - dy}")
