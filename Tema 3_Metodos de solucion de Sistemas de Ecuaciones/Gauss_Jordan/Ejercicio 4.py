n = int(input("cuantas incognitas: "))

print("ingresa la matriz aumentada")
A = []
for i in range(n):
    fila = list(map(float, input().split()))
    A.append(fila)

print("matriz antes:")
for f in A:
    print(f)

for i in range(n):
    if A[i][i] == 0:
        for k in range(i+1, n):
            if A[k][i] != 0:
                A[i], A[k] = A[k], A[i]
                break

    div = A[i][i]
    for j in range(n+1):
        A[i][j] = A[i][j] / div

    for k in range(n):
        if k != i:
            mult = A[k][i]
            for j in range(n+1):
                A[k][j] = A[k][j] - mult * A[i][j]

    print(f"despues de columna {i+1}:")
    for f in A:
        print([round(x, 3) for x in f])

print("resultados finales:")
for i in range(n):
    print(f"x{i+1} =", round(A[i][n], 5))
