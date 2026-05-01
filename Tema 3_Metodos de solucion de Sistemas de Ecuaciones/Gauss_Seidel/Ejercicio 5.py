n = int(input("tamaño del sistema: "))

A = []
b = []
for i in range(n):
    fila = list(map(float, input(f"fila {i+1} con resultado: ").split()))
    b.append(fila[-1])
    A.append(fila[:-1])

x = [0.0] * n
error = 1
iteracion = 0

while error > 1e-6 and iteracion < 100:
    error = 0
    for i in range(n):
        xnuevo = b[i]
        for j in range(n):
            if j != i:
                xnuevo = xnuevo - A[i][j] * x[j]
        xnuevo = xnuevo / A[i][i]

        if x[i] != 0:
            e = abs(xnuevo - x[i]) / abs(x[i])
            if e > error:
                error = e
        x[i] = xnuevo

    iteracion = iteracion + 1
    print("iteracion", iteracion, "->", [round(v, 4) for v in x])

print("solucion final:")
for i in range(n):
    print(f"x{i+1} =", round(x[i], 7))
print("total de iteraciones:", iteracion)
