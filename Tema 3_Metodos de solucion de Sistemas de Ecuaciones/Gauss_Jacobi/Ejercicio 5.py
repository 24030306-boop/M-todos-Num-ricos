n = int(input("tamaño: "))

A = []
b = []
print("ingresa cada fila con su resultado al final")
for i in range(n):
    fila = list(map(float, input().split()))
    A.append(fila[:n])
    b.append(fila[n])

x = [0.0] * n
iteracion = 0
sigue = True

while sigue and iteracion < 100:
    x_ant = x.copy()
    x_temp = [0.0] * n

    for i in range(n):
        s = 0.0
        for j in range(n):
            if j != i:
                s = s + A[i][j] * x_ant[j]
        x_temp[i] = (b[i] - s) / A[i][i]

    iteracion = iteracion + 1

    err_max = 0.0
    for i in range(n):
        if x_temp[i] != 0:
            e = abs((x_temp[i] - x_ant[i]) / x_temp[i])
            if e > err_max:
                err_max = e

    x = x_temp.copy()
    print(f"iteracion {iteracion}:", [round(xi, 5) for xi in x], "| error:", round(err_max, 8))

    if err_max < 1e-7:
        sigue = False

if not sigue:
    print("convergio bien")
else:
    print("no convergio")

print("solucion aproximada:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.7f}")
print("iteraciones usadas:", iteracion)
