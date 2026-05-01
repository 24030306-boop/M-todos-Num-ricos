# 7. Desbordamiento (Overflow) en Punto Flotante
import sys
import math

maximo = sys.float_info.max
print(f"Valor máximo de float: {maximo}")

resultado = maximo * 2
print(f"Resultado tras overflow: {resultado}")

if math.isinf(resultado):
    print("ERROR: Overflow detectado (infinito)")

# Underflow también es posible
minimo = sys.float_info.min
underflow = minimo / 1e308
print(f"\nUnderflow: {minimo} / 1e308 = {underflow}")
if underflow == 0.0:
    print("NOTA: Underflow — el valor colapsó a 0.0")
