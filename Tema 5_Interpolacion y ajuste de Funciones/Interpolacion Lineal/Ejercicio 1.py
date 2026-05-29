# Ejercicio 1: Interpolación Lineal - Resistencia vs Temperatura
# Puntos conocidos: (20°C, 50 Ω) y (40°C, 62 Ω)
# Estimar resistencia a 30°C

temp0, res0 = 20, 50   # Punto 1: (temperatura, resistencia)
temp1, res1 = 40, 62   # Punto 2
temp_objetivo = 30      # Temperatura a interpolar

# Interpolación lineal
pendiente = (res1 - res0) / (temp1 - temp0)
resistencia_estimada = res0 + pendiente * (temp_objetivo - temp0)

print(f"Pendiente: {pendiente} Ω/°C")
print(f"Resistencia a {temp_objetivo}°C: {resistencia_estimada} Ω")
# Resultado esperado: 56.0 Ω

