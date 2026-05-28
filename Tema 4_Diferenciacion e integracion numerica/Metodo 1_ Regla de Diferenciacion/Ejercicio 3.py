import math

def a(t):
    return 0.3 * math.sin(5 * t) * math.exp(-0.2 * t)

t0 = 0.4
h  = 0.004

# Primera derivada (velocidad) — fórmula de 5 puntos
vel = (a(t0-2*h) - 8*a(t0-h) + 8*a(t0+h) - a(t0+2*h)) / (12 * h)

# Segunda derivada (tasa de cambio de aceleración) — diferencias centradas
jerk = (-a(t0-2*h) + 16*a(t0-h) - 30*a(t0) + 16*a(t0+h) - a(t0+2*h)) / (12 * h**2)

print(f'Velocidad aprox (a prime)  : {vel:.10f} m/s²')
print(f'Jerk aprox     (a double ) : {jerk:.10f} m/s³')

