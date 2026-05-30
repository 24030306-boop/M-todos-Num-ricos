# dP/dt = r*P*(1 - P/K),  P(0) = 50
r = 0.3
K = 1000

def f(t, P):
    return r * P * (1 - P / K)

def euler(f, t0, P0, h, n):
    t, P = t0, P0
    datos = [(t, P)]
    for _ in range(n):
        P = P + h * f(t, P)
        t += h
        datos.append((t, round(P, 4)))
    return datos

datos = euler(f, t0=0, P0=50, h=1, n=30)

print(f"{'Año':>4} {'Población':>12}")
for t, P in datos[::3]:
    barra = '█' * int(P / 30)
    print(f"{t:4.0f} {P:12.1f} {barra}")

print(f"Población final ≈ {datos[-1][1]:.1f}  (K = {K})")
