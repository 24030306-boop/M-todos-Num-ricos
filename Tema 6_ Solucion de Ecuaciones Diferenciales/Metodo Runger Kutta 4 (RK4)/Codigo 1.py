# Aleta rectangular: dT/dx=q, dq/dx=m²*(T-T_inf)
h_c=25; P=0.04; A=0.0001; k_a=200; T_inf=25
m2 = (h_c * P) / (k_a * A)

def f(x, T, q):
    return q, m2 * (T - T_inf)

def heun(x0, T0, q0, h, x_final):
    x, T, q = x0, T0, q0
    datos = [(x, T)]
    while x < x_final:
        k1T, k1q = f(x, T, q)
        Tp = T + h * k1T
        qp = q + h * k1q
        k2T, k2q = f(x+h, Tp, qp)
        T = T + (h/2)*(k1T + k2T)
        q = q + (h/2)*(k1q + k2q)
        x = round(x + h, 10)
        datos.append((x, T))
    return datos

res = heun(x0=0, T0=100, q0=0, h=0.005, x_final=0.1)
print(f"{'x(m)':>7} {'T(°C)':>8}")
for x, T in res[::4]:
    print(f"{x:7.4f} {T:8.4f}")
