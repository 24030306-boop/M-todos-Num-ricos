def f(x):
    return x**3 - x - 2

def biseccion(a, b, tol=1e-10, max_iter=100):
    if f(a) * f(b) >= 0:
        print("f(a)*f(b) >= 0: no se garantiza raíz en el intervalo.")
        return None
    print(f"{'Iter':>4} {'a':>14} {'b':>14} {'c':>14} {'f(a)':>14} {'f(c)':>14} {'f(a)*f(c)':>14} {'E(a)%':>10} {'E(t)':>12}")
    print("-" * 110)
    raiz_exacta = 1.5213797
    c_prev = None
    for i in range(1, max_iter + 1):
        c   = (a + b) / 2
        fa  = f(a)
        fc  = f(c)
        prod = fa * fc
        ea  = abs((c - c_prev) / c) * 100 if c_prev is not None else 0
        et  = abs((raiz_exacta - c) / raiz_exacta) * 100
        print(f"{i:>4} {a:>14.8f} {b:>14.8f} {c:>14.8f} {fa:>14.8f} {fc:>14.8f} {prod:>14.8f} {ea:>10.6f} {et:>12.8f}")
        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\nRaíz aproximada: {c:.10f} en {i} iteraciones")
            return c
        c_prev = c
        if prod < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

biseccion(1, 2)
