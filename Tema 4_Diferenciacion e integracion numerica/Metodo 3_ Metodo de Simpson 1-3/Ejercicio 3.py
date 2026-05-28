def Cp(T):
    return 29.1 - 0.0015 * T + 8e-6 * T**2

def simpson_quimica(func, a, b, n):
    h    = (b - a) / n
    acum = func(a) + func(b)
    for i in range(1, n):
        acum += (4 if i % 2 != 0 else 2) * func(a + i * h)
    return (h / 3) * acum

calor_Q = simpson_quimica(Cp, 400, 700, 12)
print(f'Calor absorbido Q: {calor_Q:.6f} kJ/mol')

