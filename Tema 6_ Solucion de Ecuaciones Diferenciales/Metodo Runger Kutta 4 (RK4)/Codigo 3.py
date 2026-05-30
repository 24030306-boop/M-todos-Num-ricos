# RK4: 4 pendientes ponderadas (1,2,2,1)/6
import math

def f(x, y):
    return y

def rk4_paso(f, x, y, h):
    k1 = f(x,       y          )
    k2 = f(x+h/2, y+h*k1/2)
    k3 = f(x+h/2, y+h*k2/2)
    k4 = f(x+h,   y+h*k3    )
    return y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

def rk4(f, x0, y0, h, n):
    x, y = x0, y0
    res = [(x, y)]
    for _ in range(n):
        y = rk4_paso(f, x, y, h)
        x += h
        res.append((x, y))
    return res

res = rk4(f, 0, 1, 0.2, 5)

print(f"{'x':>4} {'RK4':>14} {'Exacta':>14} {'Error':>14}")
for x, y in res:
    e = math.exp(x)
    print(f"{x:4.1f} {y:14.10f} {e:14.10f} {abs(y-e):14.2e}")
