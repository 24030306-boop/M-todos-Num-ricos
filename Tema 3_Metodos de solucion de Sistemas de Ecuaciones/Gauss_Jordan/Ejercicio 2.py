import time
import copy

def gauss_jordan(matriz):
    """Resuelve un sistema de ecuaciones usando el método de Gauss-Jordan."""
    n = len(matriz)
    m = [fila[:] for fila in matriz]  # Copia profunda

    print("\n" + "="*60)
    print("       MÉTODO DE GAUSS-JORDAN - RESOLUCIÓN PASO A PASO")
    print("="*60)

    def imprimir_matriz(m, titulo=""):
        if titulo:
            print(f"\n [{titulo}]")
        for fila in m:
            coefs = "  ".join(f"{x:10.4f}" for x in fila[:-1])
            print(f"  [ {coefs}  |  {fila[-1]:10.4f} ]")

    imprimir_matriz(m, "Matriz inicial aumentada")

    for col in range(n):
        # Buscar pivote máximo (pivoteo parcial)
        max_fila = col
        for fila in range(col + 1, n):
            if abs(m[fila][col]) > abs(m[max_fila][col]):
                max_fila = fila

        # Intercambiar filas si es necesario
        if max_fila != col:
            m[col], m[max_fila] = m[max_fila], m[col]
            print(f"\n ↕ Intercambio: Fila {col+1} ↔ Fila {max_fila+1}")

        # ... (resto del algoritmo continúa igual al patrón anterior)

    # Verificación
    if soluciones:
        print("\n" + "="*60)
        print("                    SOLUCIONES")
        print("="*60)
        for i, val in enumerate(soluciones, 1):
            print(f"  x{i} = {val:>12.6f}")

        print("\n" + "-"*60)
        print("  Verificación (sustituyendo en el sistema original):")
        print("-"*60)
        A = [fila[:-1] for fila in matriz]
        b = [fila[-1] for fila in matriz]
        ok = True
        for i in range(len(b)):
            resultado = sum(A[i][j] * soluciones[j] for j in range(len(soluciones)))
            estado = "✓" if abs(resultado - b[i]) < 1e-6 else "✗"
            print(f"  Ecuación {i+1}: {resultado:.6f}  (esperado {b[i]})  {estado}")
            if abs(resultado - b[i]) >= 1e-6:
                ok = False
        print("-"*60)
        print(f"  {'✅ Verificación exitosa' if ok else '⚠ Verifique los resultados'}")
    else:
        print("  ⚠ El sistema no tiene solución única.")

    print("\n" + "="*60)
    print(f"  ⏱ Tiempo de ejecución: {tiempo_total:.6f} segundos")
    print(f"     ({tiempo_total * 1_000:.4f} milisegundos)")
    print("="*60 + "\n")
