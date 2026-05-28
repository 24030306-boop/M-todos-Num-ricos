import math

def f(x):
    return math.log(x)

x0 = 0.005
h  = 0.01

try:
    aprox = (f(x0 + h) - f(x0 - h)) / (2 * h)
    print(f'Resultado: {aprox:.6f}')
except ValueError as e:
    print(f'ERROR de dominio: {e}')
    print('El punto x0 - h cae fuera del dominio de ln(x).')
    print('Solución: usar un h menor que x0, por ejemplo h = 0.001.')

