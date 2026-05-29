# Ejercicio 3: Extrapolación Cuadrática - Velocidad proyectada
# Puntos: (0,3), (2,11), (4,27) → proyectar t=6

x0, y0 = 0, 3
x1, y1 = 2, 11
x2, y2 = 4, 27
x_obj = 6

b0 = y0
b1 = (y1 - y0) / (x1 - x0)
b2 = (((y2 - y1) / (x2 - x1)) - b1) / (x2 - x0)

velocidad = b0 + b1*(x_obj - x0) + b2*(x_obj - x0)*(x_obj - x1)

print(f"Velocidad a t={x_obj} s: {velocidad} m/s")
# Resultado esperado: 51 m/s

