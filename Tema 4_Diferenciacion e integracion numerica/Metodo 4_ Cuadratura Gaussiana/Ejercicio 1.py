import math
L = 4.0

def q(x):
    return 5000 * math.sin(math.pi * x / L)
def gauss_3puntos(func, a, b):
    # Nodos y pesos de Gauss-Legendre para n = 3
    nodos  = [-0.7745966692, 0.0, 0.7745966692]
    pesos  = [ 0.5555555556, 0.8888888889, 0.5555555556]
    factor = 0.5 * (b - a)
    centro = 0.5 * (b + a)
    suma   = 0.0
    for xi, wi in zip(nodos, pesos):
        t    = factor * xi + centro
        suma += wi * func(t)
    return factor * suma

carga_total = gauss_3puntos(q, 0, L)
print(f'Carga total integrada: {carga_total:.6f} N')

