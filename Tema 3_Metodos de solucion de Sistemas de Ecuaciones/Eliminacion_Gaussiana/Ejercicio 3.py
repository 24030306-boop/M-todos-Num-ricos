import numpy as np

n = int(input("cuantas variables: "))
A = []
for i in range(n):
    fila = list(map(float, input(f"fila {i+1}: ").split()))
    A.append(fila)
b = list(map(float, input("vector b: ").split()))

Ab = []
for i in range(n):
    Ab.append(A[i] + [b[i]])

for i in range(n):
    for k in range(i+1, n):
        if Ab[k][i] != 0:
            factor = Ab[k][i] / Ab[i][i]
            for j in range(n+1):
                Ab[k][j] = Ab[k][j] - factor * Ab[i][j]

x = [0] * n
for i in range(n-1, -1, -1):
    x[i] = Ab[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - Ab[i][j] * x[j]
    x[i] = x[i] / Ab[i][i]

print("soluciones:")
for i in range(n):
    print(f"x{i+1} =", round(x[i], 4))
