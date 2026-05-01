def f(x):
    return x**2 - 3

def falsa_posicion(a, b, tol=1e-10, max_iter=100):
    if f(a) * f(b) >= 0:
        print("f(a)*f(b) >= 0: no se garantiza raíz en el intervalo.")
        return None
    print(f"{'Iter':>4} {'a':>14} {'b':>14} {'c':>14} {'f(a)':>14} {'f(c)':>14} {'f(a)*f(c)':>14} {'E(a)%':>10}")
    print("-" * 100)
    c_prev = None
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c  = b - fb * (a - b) / (fa - fb)
        fc = f(c)
        prod = fa * fc
        ea = abs((c - c_prev) / c) * 100 if c_prev is not None else 0
        print(f"{i:>4} {a:>14.8f} {b:>14.8f} {c:>14.8f} {fa:>14.8f} {fc:>14.8f} {prod:>14.8f} {ea:>10.6f}")
        if abs(fc) < tol or (c_prev is not None and abs(c - c_prev) < tol):
            print(f"\nRaíz aproximada: {c:.10f} en {i} iteraciones")
            return c
        c_prev = c
        if prod < 0:
            b = c
        else:
            a = c
    return c

falsa_posicion(1, 2)
