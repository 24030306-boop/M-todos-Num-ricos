# Ejercicio 5: Spline Lineal - Nodos (1,4), (3,10), (7,22)

nodos = [(1, 4), (3, 10), (7, 22)]

def spline_lineal(nodos, x_obj):
    for i in range(len(nodos) - 1):
        x0, y0 = nodos[i]
        x1, y1 = nodos[i + 1]
        if x0 <= x_obj <= x1:
            m = (y1 - y0) / (x1 - x0)
            return y0 + m * (x_obj - x0)
    return None  # Fuera del dominio

for x_eval in [2, 5]:
    val = spline_lineal(nodos, x_eval)
    print(f"S({x_eval}) = {val}")
# Resultado esperado: S(2)=7, S(5)=16

