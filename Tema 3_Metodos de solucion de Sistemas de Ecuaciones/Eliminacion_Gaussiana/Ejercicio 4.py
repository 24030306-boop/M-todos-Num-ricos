import numpy as np

print("ingresa el sistema de ecuaciones")
n = int(input("numero de ecuaciones: "))

matriz = []
for i in range(n):
    fila = list(map(float, input(f"ecuacion {i+1} (coeficientes y resultado): ").split()))
    matriz.append(fila)

print("matriz inicial")
for fila in matriz:
    print(fila)

for col in range(n):
    pivote = col
    for fila in range(col+1, n):
        if abs(matriz[fila][col]) > abs(matriz[pivote][col]):
            pivote = fila
    matriz[col], matriz[pivote] = matriz[pivote], matriz[col]

    for fila in range(col+1, n):
        if matriz[col][col] == 0:
            print("no se puede resolver")
            break
        factor = matriz[fila][col] / matriz[col][col]
        for j in range(col, n+1):
            matriz[fila][j] = matriz[fila][j] - factor * matriz[col][j]

print("matriz triangular")
for fila in matriz:
    print([round(x, 4) for x in fila])

x = [0.0] * n
for i in range(n-1, -1, -1):
    suma = 0
    for j in range(i+1, n):
        suma = suma + matriz[i][j] * x[j]
    x[i] = (matriz[i][n] - suma) / matriz[i][i]

print("resultados:")
for i in range(n):
    print(f"x{i+1} = {round(x[i], 6)}")
