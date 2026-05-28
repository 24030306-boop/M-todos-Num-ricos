import numpy as np

def f_rayleigh(x):
    return x * np.exp(-x**2 / 2)

def gauss_legendre(func, a, b, n=5):
    nodos, pesos = np.polynomial.legendre.leggauss(n)
    factor  = 0.5 * (b - a)
    centro  = 0.5 * (b + a)
    puntos  = factor * nodos + centro
    return factor * np.sum(pesos * func(puntos))

prob = gauss_legendre(f_rayleigh, 0.5, 2.0, n=5)
print(f'P(0.5 < X < 2.0) = {prob:.8f}')
