def verificar_simpson(n):
    if n % 2 != 0:
        return (f'ERROR: Simpson 1/3 exige un numero PAR de subintervalos. '
                f'n = {n} es impar. Ajuste a n = {n + 1} o n = {n - 1}.')
    return 'Parámetros válidos. Procediendo con el cálculo...'

print(verificar_simpson(9))

