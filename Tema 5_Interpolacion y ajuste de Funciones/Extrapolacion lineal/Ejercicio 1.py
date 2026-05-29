# Ejercicio 1: Extrapolación Lineal - Demanda eléctrica
# Datos: (2018, 320 MW), (2022, 380 MW) → proyectar 2025

anio0, demanda0 = 2018, 320
anio1, demanda1 = 2022, 380
anio_obj = 2025

pendiente = (demanda1 - demanda0) / (anio1 - anio0)
demanda_proj = demanda1 + pendiente * (anio_obj - anio1)

print(f"Pendiente: {pendiente} MW/año")
print(f"Demanda proyectada en {anio_obj}: {demanda_proj} MW")
# Resultado esperado: 425 MW

