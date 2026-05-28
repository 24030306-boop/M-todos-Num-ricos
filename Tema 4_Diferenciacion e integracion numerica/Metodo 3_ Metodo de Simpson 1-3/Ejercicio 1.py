import math

def F(x):
    return x**3 * math.cos(x / 2) + 15

def simpson_tercio(func, a, b, n):
    if n % 2 != 0:
        raise ValueError('n debe ser par para Simpson 1/3')
    h    = (b - a) / n
    acum = func(a) + func(b)
    for i in range(1, n):
        coef = 4 if i % 2 != 0 else 2
        acum += coef * func(a + i * h)
    return (h / 3) * acum

trabajo = simpson_tercio(F, 0, 8, 16)
print(f'Trabajo realizado: {trabajo:.6f} J')

