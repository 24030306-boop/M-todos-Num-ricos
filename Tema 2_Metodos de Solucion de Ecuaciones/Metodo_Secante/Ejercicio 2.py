def f(x):
    return x**3 - 2*x - 5

def secante(x0, x1, tol=1e-10, max_iter=100):
    print(f"{'n':>3} {'Xi-1':>16} {'Xi':>16} {'f(Xi-1)':>16} {'f(Xi)':>16} {'Xi+1':>16} {'er%':>12}")
    print("-" * 95)
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("División por cero — sin solución.")
            return None
        x2  = x1 - fx1 * (x0 - x1) / (fx0 - fx1)
        err = abs((x2 - x1) / x2) * 100 if x2 != 0 else 0
        print(f"{i:>3} {x0:>16.10f} {x1:>16.10f} {fx0:>16.10f} {fx1:>16.10f} {x2:>16.10f} {err:>12.6f}")
        if abs(x2 - x1) < tol:
            print(f"\nRaíz encontrada: {x2:.10f} en {i} iteraciones")
            return x2
        x0, x1 = x1, x2
    print("No convergió.")
    return None

secante(2, 3)
