# Heun: predictor-corrector con promedio de pendientes
import math

def f(x, y):
    return y

def heun(f, x0, y0, h, n):
    x, y = x0, y0
    res = [(x, y)]
    for _ in range(n):
        k1 = f(x, y)
        y_pred = y + h * k1          # predictor
        k2 = f(x + h, y_pred)
        y = y + (h / 2) * (k1 + k2) # corrector
        x += h
        res.append((x, y))
    return res

def euler(f, x0, y0, h, n):
    x, y = x0, y0
    res = [(x, y)]
    for _ in range(n):
        y = y + h * f(x, y)
        x += h
        res.append((x, y))
    return res

h, n = 0.2, 5
rh = heun(f, 0, 1, h, n)
re = euler(f, 0, 1, h, n)

print(f"{'x':>4} {'Exacta':>10} {'Euler':>10} {'Heun':>10}")
for i in range(n+1):
    x = rh[i][0]
    print(f"{x:4.1f} {math.exp(x):10.6f} {re[i][1]:10.6f} {rh[i][1]:10.6f}")
