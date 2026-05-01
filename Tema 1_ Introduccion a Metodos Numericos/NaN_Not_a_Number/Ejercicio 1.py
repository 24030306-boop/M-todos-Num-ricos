# 8. NaN (Not a Number)
import math

a = 0.0
b = 0.0

# Python lanza ZeroDivisionError en vez de NaN — lo manejamos
try:
    resultado = a / b
except ZeroDivisionError:
    resultado = float("nan")
    print("ZeroDivisionError capturado → se asigna NaN manualmente")

print(f"Resultado: {resultado}")

if math.isnan(resultado):
    print("ERROR: Resultado indefinido (NaN)")

# Otras operaciones que producen NaN directamente
nan1 = float("inf") - float("inf")
nan2 = float("inf") * 0
print(f"\ninf - inf = {nan1}  → isnan: {math.isnan(nan1)}")
print(f"inf * 0   = {nan2}  → isnan: {math.isnan(nan2)}")
