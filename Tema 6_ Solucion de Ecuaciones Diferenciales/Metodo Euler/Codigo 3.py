# x'' + w²x = 0  →  x' = v,  v' = -w²x
import math

w = 2  # frecuencia angular

def sistema(t, x, v):
    return v, -(w**2) * x

def euler_sistema(t0, x0, v0, h, n):
    t, x, v = t0, x0, v0
    tray = [(t, x, v)]
    for _ in range(n):
        dx, dv = sistema(t, x, v)
        x = x + h * dx
        v = v + h * dv
        t = t + h
        tray.append((t, x, v))
    return tray

res = euler_sistema(t0=0, x0=1, v0=0, h=0.05, n=100)

print(f"{'t':>6} {'x_euler':>10} {'x_exacta':>10} {'error':>10}")
for t, x, v in res[::10]:
    x_e = math.cos(w * t)
    print(f"{t:6.2f} {x:10.5f} {x_e:10.5f} {abs(x-x_e):10.5f}")
