n = int(input("numero de variables: "))

A = []
for i in range(n):
    fila = list(map(float, input(f"fila {i+1}: ").split()))
    A.append(fila)
b = list(map(float, input("vector b: ").split()))

x = [0.0] * n
tol = 1e-6
max_iter = 100

for it in range(max_iter):
    x_nuevo = [0.0] * n

    for i in range(n):
        suma = b[i]
        for j in range(n):
            if j != i:
                suma = suma - A[i][j] * x[j]
        x_nuevo[i] = suma / A[i][i]

    error = 0
    for i in range(n):
        if x_nuevo[i] != 0:
            e = abs((x_nuevo[i] - x[i]) / x_nuevo[i]) * 100
            if e > error:
                error = e

    x = x_nuevo.copy()
    print(f"iter {it+1}: {[round(v, 5) for v in x]} error={round(error,5)}")

    if error < tol:
        print(f"convergio en {it+1} iteraciones")
        break

print("solucion:")
for i in range(n):
    print(f"x{i+1} = {round(x[i], 6)}")
