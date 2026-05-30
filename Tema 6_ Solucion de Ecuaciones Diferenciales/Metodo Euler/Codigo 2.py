# dT/dt = -k*(T - T_amb),  T(0) = 90°C
k = 0.1
T_amb = 20

def f(t, T):
    return -k * (T - T_amb)

def euler(f, t0, y0, h, t_final):
    t, y = t0, y0
    while t <= t_final:
        print(f"t={t:.1f}  T={y:.4f}°C")
        y = y + h * f(t, y)
        t = t + h

euler(f, t0=0, y0=90, h=0.5, t_final=10)

import math
T_exacta = T_amb + (90 - T_amb) * math.exp(-k * 10)
print(f"Solución exacta en t=10: T = {T_exacta:.4f}°C")
