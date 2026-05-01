import numpy as np

n = int(input("tamaño del sistema: "))

print("ingresa la matriz aumentada fila por fila")
M = []
for i in range(n):
    fila = list(map(float, input().split()))
    M.append(fila)

# eliminacion sin pivoteo
for i in range(n):
    for k in range(i+1, n):
        factor = M[k][i] / M[i][i]
        for j in range(n+1):
            M[k][j] = M[k][j] - factor * M[i][j]

print("matriz despues de eliminacion:")
for f in M:
    print([round(v, 3) for v in f])

# sustitucion hacia atras
x = [0.0] * n
for i in range(n-1, -1, -1):
    x[i] = M[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - M[i][j] * x[j]
    x[i] = x[i] / M[i][i]

print("\nla solucion es:")
for i in range(n):
    print("x" + str(i+1) + " = " + str(round(x[i], 5)))
