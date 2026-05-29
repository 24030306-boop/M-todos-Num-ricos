# Ejercicio 2: Correlación - Voltaje (V) vs Corriente (A)
# Datos: (2,0.4), (4,0.8), (6,1.2)

import math

voltaje  = [2, 4, 6]
corriente = [0.4, 0.8, 1.2]
n = len(voltaje)

sum_x  = sum(voltaje)
sum_y  = sum(corriente)
sum_xy = sum(voltaje[i]*corriente[i] for i in range(n))
sum_x2 = sum(x**2 for x in voltaje)
sum_y2 = sum(y**2 for y in corriente)

num = n*sum_xy - sum_x*sum_y
den = math.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))
r = num / den

print(f"r = {r:.4f}")
# Resultado esperado: r = 1.0000

