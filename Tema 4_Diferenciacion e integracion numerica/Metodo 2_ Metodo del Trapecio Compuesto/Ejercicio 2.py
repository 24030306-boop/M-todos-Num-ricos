import math

def g(omega):
    return 1 / math.sqrt(omega)   # indefinida en omega = 0

def trapecio_erroneo(func, a, b, n):
    h = (b - a) / n
    try:
        acum = (func(a) + func(b)) / 2   # falla aqui: func(0) -> error
        for k in range(1, n):
            acum += func(a + k * h)
        return acum * h
    except (ValueError, ZeroDivisionError) as e:
        return f'ERROR: {e}. La función no está definida en x = {a}.'

print(trapecio_erroneo(g, 0, 4, 80))

