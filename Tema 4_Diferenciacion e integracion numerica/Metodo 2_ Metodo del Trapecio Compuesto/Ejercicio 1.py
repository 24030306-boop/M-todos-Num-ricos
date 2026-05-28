import math

def v(x):
    return 2 + 0.5 * x * math.cos(x)

def energia(x):
    return v(x)**2 / 2

def trapecio_compuesto(func, a, b, n):
    h    = (b - a) / n
    acum = (func(a) + func(b)) / 2
    for k in range(1, n):
        acum += func(a + k * h)
    return acum * h

resultado = trapecio_compuesto(energia, 0, 6, 120)
print(f'Energía cinética total: {resultado:.6f} J/m')

