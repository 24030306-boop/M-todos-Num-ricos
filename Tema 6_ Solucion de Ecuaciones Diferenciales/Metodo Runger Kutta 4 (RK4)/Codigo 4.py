# dC/dt = -k*C,  C(0) = 1 mol/L
import math

k = 0.5

def f(t, C):
    return -k * C

def rk4(f, t0, C0, h, n):
    t, C = t0, C0
    datos = []
    for _ in range(n+1):
        Ce = math.exp(-k*t)
        datos.append((t, C, Ce))
        k1 = f(t,      C)
        k2 = f(t+h/2, C+h*k1/2)
        k3 = f(t+h/2, C+h*k2/2)
        k4 = f(t+h,    C+h*k3)
        C += (h/6)*(k1+2*k2+2*k3+k4)
        t += h
    return datos

datos = rk4(f, 0, 1.0, 0.5, 10)

print(f"{'t(s)':>6} {'C_RK4':>12} {'C_exacta':>12} {'Error':>12}")
for t,C,Ce in datos:
    print(f"{t:6.2f} {C:12.8f} {Ce:12.8f} {abs(C-Ce):12.2e}")
print(f"Vida media = {math.log(2)/k:.4f} s")
