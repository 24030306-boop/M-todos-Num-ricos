#Ejercicio 3: Interpolación Cuadrática - Polinomio de Newton
# Puntos: (2, 5), (4, 17), (6, 37) → estimar f(5)

x0, y0 = 2, 5
x1, y1 = 4, 17
x2, y2 = 6, 37
x_obj = 5

# Coeficientes de diferencias divididas
b0 = y0
b1 = (y1 - y0) / (x1 - x0)
b2 = (((y2 - y1) / (x2 - x1)) - b1) / (x2 - x0)

# Evaluación del polinomio
resultado = b0 + b1*(x_obj - x0) + b2*(x_obj - x0)*(x_obj - x1)

print(f"b0={b0}, b1={b1}, b2={b2}")
print(f"f({x_obj}) = {resultado}")
# Resultado esperado: 26

