import math

def f_abs(x):
    return abs(x - 1)

def gauss_3puntos(func, a, b):
    nodos  = [-0.7745966692, 0.0, 0.7745966692]
    pesos  = [ 0.5555555556, 0.8888888889, 0.5555555556]
    factor = 0.5 * (b - a)
    centro = 0.5 * (b + a)
    suma   = sum(wi * func(factor*xi + centro) for xi, wi in zip(nodos, pesos))
    return factor * suma

# Valor exacto = 1.0 (simetria del valor absoluto en [0,2])
aprox   = gauss_3puntos(f_abs, 0, 2)
exacto  = 1.0
error   = abs(aprox - exacto) / exacto * 100

print(f'Resultado Gauss     : {aprox:.8f}')
print(f'Valor exacto        : {exacto:.8f}')
print(f'Error relativo      : {error:.4f} %')
print('ADVERTENCIA: Error elevado por quiebre en x=1.')
print('Aplicar Gauss por subintervalos: [0,1] y [1,2].')

