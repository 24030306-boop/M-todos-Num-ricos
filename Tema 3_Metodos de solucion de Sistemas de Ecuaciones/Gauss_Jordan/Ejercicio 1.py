import numpy as np

np.set_printoptions(precision=2, suppress=True, linewidth=200)

def resolver_gauss_jordan_10x10():
    n = 10

    # Matriz A: Diagonal con 10s, resto con 1s
    A = np.ones((n, n)) + np.diag([9]*n)
    # Vector B: Resultados del 10 al 100
    B = np.arange(10, 110, 10).astype(float)

    Ab = np.hstack([A, B.reshape(-1, 1)])

    print("ESTADO INICIAL: MATRIZ AUMENTADA (10x11)")
    print(Ab)
    print("-" * 100)

    for i in range(n):
        # PASO 2: Pivoteo
        fila_max = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, fila_max]] = Ab[[fila_max, i]]

        # PASO 3: Normalización
        pivote = Ab[i, i]
        Ab[i] = Ab[i] / pivote

        # PASO 4: Eliminación
        for j in range(n):
            if i != j:
                factor = Ab[j, i]
                Ab[j] = Ab[j] - factor * Ab[i]

        # Mostrar estado intermedio en la iteración 5
        if i == 4:
            print(f"ESTADO INTERMEDIO: COLUMNA {i+1} PROCESADA")
            print(Ab)
            print("-" * 100)

    print("ESTADO FINAL: MATRIZ EN FORMA ESCALONADA REDUCIDA (IDENTIDAD)")
    print(Ab)

    return Ab[:, -1]

try:
    soluciones = resolver_gauss_jordan_10x10()
    print("\n" + "-"*40)
    print("RESULTADOS FINALES (Valores de x1 a x10)")
    print("="*40)
    for idx, sol in enumerate(soluciones):
        print(f"x{idx+1:02d} = {sol:8.4f}")
    print("="*40)
except Exception as e:
    print(f"Error durante la ejecución: {e}")
