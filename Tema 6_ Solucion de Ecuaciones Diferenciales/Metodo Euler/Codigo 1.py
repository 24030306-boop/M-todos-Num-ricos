def f(x, y):
    return y

def euler(f, x0, y0, h, n):
    x, y = x0, y0
    resultados = [(x, y)]
    for _ in range(n):
        y = y + h * f(x, y)  # y_{n+1} = y_n + h*f(x_n, y_n)
        x = x + h
        resultados.append((x, y))
    return resultados

x0, y0 = 0, 1
h = 0.1
n = 10
resultados = euler(f, x0, y0, h, n)

import math
print(f"{'x':>6} {'y_euler':>12} {'y_exacta':>12} {'error':>12}")
for x, y in resultados:
    exacta = math.exp(x)
    error = abs(exacta - y)
    print(f"{x:6.2f} {y:12.6f} {exacta:12.6f} {error:12.6f}")
