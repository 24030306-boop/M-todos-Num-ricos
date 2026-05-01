n = int(input("cuantas variables: "))

coef = []
for i in range(n):
    fila = list(map(float, input(f"ecuacion {i+1}: ").split()))
    coef.append(fila)

resultado = list(map(float, input("resultados: ").split()))

x = [0.0] * n
limite = 50
tolerancia = 1e-5

for it in range(limite):
    x_ant = x.copy()

    for i in range(n):
        acum = resultado[i]
        for j in range(n):
            if i != j:
                acum = acum - coef[i][j] * x[j]
        x[i] = acum / coef[i][i]

    convergio = True
    for i in range(n):
        if x[i] != 0:
            if abs((x[i] - x_ant[i]) / x[i]) * 100 > tolerancia:
                convergio = False
                break

    if convergio:
        print(f"convergio en {it+1} iteraciones")
        break
else:
    print("no convergio")

for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")
