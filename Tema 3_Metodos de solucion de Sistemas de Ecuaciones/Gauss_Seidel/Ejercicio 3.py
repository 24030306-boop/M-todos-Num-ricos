n = int(input("numero de ecuaciones: "))

A = []
for i in range(n):
    fila = list(map(float, input(f"fila {i+1}: ").split()))
    A.append(fila)
b = list(map(float, input("vector b: ").split()))

x = [0.0] * n
tol = 0.0001
iteraciones = 0
max_iter = 100

while iteraciones < max_iter:
    x_viejo = x.copy()

    for i in range(n):
        suma = b[i]
        for j in range(n):
            if j != i:
                suma = suma - A[i][j] * x[j]
        x[i] = suma / A[i][i]

    error = 0
    for i in range(n):
        if x[i] != 0:
            e = abs((x[i] - x_viejo[i]) / x[i]) * 100
            if e > error:
                error = e

    iteraciones = iteraciones + 1
    print(f"iteracion {iteraciones}: {[round(v, 5) for v in x]} error={round(error, 5)}")

    if error < tol:
        break

print("resultado:")
for i in range(n):
    print(f"x{i+1} = {round(x[i], 6)}")
print("iteraciones:", iteraciones)
