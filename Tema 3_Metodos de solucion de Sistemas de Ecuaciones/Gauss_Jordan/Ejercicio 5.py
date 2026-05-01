import numpy as np

n = int(input("tamaño: "))
Ab = np.zeros((n, n+1))

for i in range(n):
    fila = list(map(float, input(f"fila {i+1}: ").split()))
    for j in range(n+1):
        Ab[i][j] = fila[j]

for i in range(n):
    max_fila = i
    for k in range(i+1, n):
        if abs(Ab[k][i]) > abs(Ab[max_fila][i]):
            max_fila = k
    Ab[[i, max_fila]] = Ab[[max_fila, i]]

    Ab[i] = Ab[i] / Ab[i][i]

    for k in range(n):
        if k != i:
            Ab[k] = Ab[k] - Ab[k][i] * Ab[i]

print("la solucion del sistema es:")
for i in range(n):
    print("x" + str(i+1) + " = " + str(round(Ab[i][n], 6)))
