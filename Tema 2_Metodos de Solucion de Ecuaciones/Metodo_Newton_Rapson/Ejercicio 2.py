def f(x):
    return x**5 - x - 1

def df(x):
    return 5 * x**4 - 1

def newton_raphson(x0, tol=1e-10, max_iter=100):
    xi = x0
    print(f"{'Iter':>4} {'xi':>18} {'f(xi)':>18} {'f\'(xi)':>18} {'xi+1':>18} {'Error%':>12}")
    print("-" * 90)
    for i in range(1, max_iter + 1):
        fxi  = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            print("Derivada cero — sin solución.")
            return None
        xi1  = xi - fxi / dfxi
        err  = abs((xi1 - xi) / xi1) * 100 if xi1 != 0 else 0
        print(f"{i:>4} {xi:>18.10f} {fxi:>18.10f} {dfxi:>18.10f} {xi1:>18.10f} {err:>12.6f}")
        if abs(xi1 - xi) < tol:
            print(f"\nRaíz encontrada: {xi1:.10f} en {i} iteraciones")
            return xi1
        xi = xi1
    print("No convergió.")
    return None

newton_raphson(1.5)
