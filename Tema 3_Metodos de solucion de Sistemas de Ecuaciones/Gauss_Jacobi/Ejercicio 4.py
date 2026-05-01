n = int(input("cuantas incognitas: "))

matriz = []
for i in range(n):
    fila = list(map(float, input(f"ecuacion {i+1} con b: ").split()))
    matriz.append(fila)

A = []
b = []
for i in range(n):
    b.append(matriz[i][n])
    A.append(matriz[i][:n])

x_viejo = [0.0] * n
iteracion = 0
max_iteraciones = 200
tolerancia = 0.00001

while iteracion < max_iteraciones:
    x_nuevo = [0.0] * n

    for i in range(n):
        total = b[i]
        for j in range(n):
            if j != i:
                total = total - A[i][j] * x_viejo[j]
        x_nuevo[i] = total / A[i][i]

    maximo_error = 0
    for i in range(n):
        if x_nuevo[i] != 0:
            err = abs(x_nuevo[i] - x_viejo[i]) / abs(x_nuevo[i])
            if err > maximo_error:
                maximo_error = err

    iteracion = iteracion + 1
    print("iteracion " + str(iteracion) + ":", [round(v, 4) for v in x_nuevo])

    if maximo_error < tolerancia:
        print("el metodo convergio")
        break

    x_viejo = x_nuevo.copy()

print("resultados:")
for i in range(n):
    print("x" + str(i+1) + " = " + str(round(x_nuevo[i], 6)))
