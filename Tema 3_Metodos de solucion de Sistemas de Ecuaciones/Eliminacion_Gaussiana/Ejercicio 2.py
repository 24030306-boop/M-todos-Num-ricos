import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
    # Formar matriz aumentada
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])
    
    print("=" * 50)
    print("MATRIZ AUMENTADA INICIAL:")
    print(Ab)
    print("=" * 50)
    
    # Eliminación hacia adelante
    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
            print(f"\n↕ Intercambio: Fila {i+1} ↔ Fila {max_row+1}")
            print(Ab)
        
        # Verificar singularidad
        if abs(Ab[i, i]) < 1e-10:
            print("Error: El sistema no tiene solución única.")
            return None
        
        # Eliminación
        for k in range(i + 1, n):
            factor = Ab[k, i] / Ab[i, i]
            Ab[k] = Ab[k] - factor * Ab[i]
            print(f"\nFila {k+1} = Fila {k+1} - ({factor:.4f}) * Fila {i+1}")
            print(Ab.round(4))
    
    print("\n" + "=" * 50)
    print("MATRIZ TRIANGULAR SUPERIOR:")
    print(Ab.round(4))
    print("=" * 50)
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, n]
        for j in range(i + 1, n):
            x[i] -= Ab[i, j] * x[j]
        x[i] /= Ab[i, i]
    
    # Verificación
    print("\nVERIFICACIÓN (Ax = b):")
    print("-" * 50)
    resultado = np.dot(A.astype(float), x)
    for i in range(n):
        estado = "✓" if abs(resultado[i] - b[i]) < 1e-6 else "✗"
        print(f"Ecuación {i+1}: {resultado[i]:.6f} (esperado {b[i]}) {estado}")
    
    # Mostrar solución
    print("\n" + "=" * 50)
    print("SOLUCIÓN:")
    print("=" * 50)
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.6f}")
    print("=" * 50)
    
    return x


# ─── MENÚ PRINCIPAL ───────────────────────────────────────
def main():
    
    print("      ELIMINACIÓN GAUSSIANA           ")
    
    
    n = int(input("\nIngrese el tamaño del sistema (n): "))
    
    print(f"\nIngrese la matriz de coeficientes A ({n}x{n}):")
    A = np.zeros((n, n))
    for i in range(n):
        fila = input(f"  Fila {i+1}: ").split()
        for j in range(n):
            A[i, j] = float(fila[j])
    
    print(f"\nIngrese el vector b ({n} valores):")
    b = np.array([float(x) for x in input("  b: ").split()])
    
    eliminacion_gaussiana(A, b)


main()
