# Ejercicio 5: Extrapolación Segmentada - Presión en tubería
# Datos: (0,200), (4,170), (8,130) kPa → estimar P(10)

nodos = [(0, 200), (4, 170), (8, 130)]

# Usar el último tramo para extrapolar
x_prev, y_prev = nodos[-2]
x_fin, y_fin   = nodos[-1]
x_obj = 10

pendiente = (y_fin - y_prev) / (x_fin - x_prev)
presion_ext = y_fin + pendiente * (x_obj - x_fin)

print(f"Pendiente último tramo: {pendiente} kPa/m")
print(f"Presión a {x_obj} m: {presion_ext} kPa")
# Resultado esperado: 110 kPa

