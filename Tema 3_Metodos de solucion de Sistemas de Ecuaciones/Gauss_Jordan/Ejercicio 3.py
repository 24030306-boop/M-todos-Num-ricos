n = int(input("numero de variables: "))

M = []
for i in range(n):
    fila = list(map(float, input(f"fila {i+1}: ").split()))
    M.append(fila)

for i in range(n):
    pivote = M[i][i]
    for j in range(n+1):
        M[i][j] = M[i][j] / pivote

    for k in range(n):
        if k != i:
            factor = M[k][i]
            for j in range(n+1):
                M[k][j] = M[k][j] - factor * M[i][j]

print("soluciones:")
for i in range(n):
    print(f"x{i+1} = {round(M[i][n], 4)}")
