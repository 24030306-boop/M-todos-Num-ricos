import numpy as np
import time

def gauss_seidel(A, b, tol=1e-6, max_iter=100, omega=1.0):
    n = len(b)
    x = np.zeros(n)
    
    
    print("        MÉTODO DE GAUSS-SEIDEL           ")
    
    
    # Verificar diagonal dominante
    print("\n📋 VERIFICACIÓN DE DIAGONAL DOMINANTE:")
    print("-" * 45)
    dominante = True
    for i in range(n):
        diagonal = abs(A[i, i])
        suma_resto = sum(abs(A[i, j]) for j in range(n) if j != i)
        estado = "✓" if diagonal > suma_resto else "✗"
        if diagonal <= suma_resto:
            dominante = False
        print(f"  Fila {i+1}: |{A[i,i]:.3f}| = {diagonal:.3f} > {suma_resto:.3f} {estado}")
    
    if not dominante:
        print("\n  La matriz NO es diagonal dominante.")
        print("    El método podría no converger.")
    else:
        print("\n  La matriz ES diagonal dominante.")
        print("    El método debería converger.")
    
    # Mostrar sistema normalizado
    print("\n📐 SISTEMA DESPEJADO:")
    print("-" * 45)
    variables = [f"x{i+1}" for i in range(n)]
    for i in range(n):
        terminos = []
        for j in range(n):
            if j != i:
                coef = -A[i, j] / A[i, i]
                signo = "+" if coef >= 0 else ""
                terminos.append(f"{signo}{coef:.4f}·{variables[j]}")
        bi = b[i] / A[i, i]
        print(f"  {variables[i]} = {bi:.4f} " + " ".join(terminos))
    
    # Encabezado tabla iteraciones
    print("\n📊 ITERACIONES:")
    print("-" * (12 * n + 20))
    encabezado = "  Iter  |" + "".join(f"  {v:^10}|" for v in variables) + "   Error    "
    print(encabezado)
    print("-" * (12 * n + 20))
    
    inicio = time.perf_counter()
    error = float('inf')
    iteracion = 0
    historial = []
    
    while error > tol and iteracion < max_iter:
        x_old = x.copy()
        
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if j != i:
                    suma -= A[i, j] * x[j]
            x_nuevo = suma / A[i, i]
            # Relajación (omega)
            x[i] = omega * x_nuevo + (1 - omega) * x_old[i]
        
        # Calcular error
        if np.any(x != 0):
            error = np.max(np.abs((x - x_old) / np.where(x != 0, x, 1))) * 100
        
        iteracion += 1
        historial.append((iteracion, x.copy(), error))
        
        # Mostrar fila de iteración
        fila = f"  {iteracion:^5}  |" + "".join(f"  {xi:^10.6f}|" for xi in x)
        fila += f"  {error:.2e}"
        print(fila)
    
    fin = time.perf_counter()
    tiempo = fin - inicio
    
    print("-" * (12 * n + 20))
    
    # Verificación
    print("\n VERIFICACIÓN (Ax = b):")
    print("-" * 45)
    resultado = np.dot(A, x)
    todo_ok = True
    for i in range(n):
        diff = abs(resultado[i] - b[i])
        estado = "✓" if diff < 1e-4 else "✗"
        if diff >= 1e-4:
            todo_ok = False
        print(f"  Ecuación {i+1}: {resultado[i]:.6f}  (esperado {b[i]:.6f})  {estado}")
    
    # Resultados finales
    print("\n" + "=" * 45)
    print("  RESULTADOS FINALES")
    print("=" * 45)
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.8f}")
    print("-" * 45)
    print(f"  Iteraciones     : {iteracion}")
    print(f"  Error final     : {error:.2e}")
    print(f"  Convergió       : {'Sí' if error <= tol else ' No'}")
    print(f"  Tiempo          : {tiempo:.6f} segundos")
    print(f"  Omega (relajac.): {omega}")
    print("=" * 45)
    
    return x, iteracion, error


# ─── MENÚ PRINCIPAL ───────────────────────────────────────
def main():
  
    print("         MÉTODO DE GAUSS-SEIDEL           ")
  
    
    n = int(input("\nIngrese el tamaño del sistema (n): "))
    
    print(f"\nIngrese la matriz de coeficientes A ({n}x{n}):")
    A = np.zeros((n, n))
    for i in range(n):
        fila = input(f"  Fila {i+1}: ").split()
        for j in range(n):
            A[i, j] = float(fila[j])
    
    print(f"\nIngrese el vector b ({n} valores):")
    b = np.array([float(x) for x in input("  b: ").split()])
    
    tol = float(input("\nIngrese la tolerancia (ej. 1e-6): ") or "1e-6")
    max_iter = int(input("Ingrese el máximo de iteraciones (ej. 100): ") or "100")
    omega = float(input("Ingrese omega para relajación (1.0 = sin relajación): ") or "1.0")
    
    gauss_seidel(A, b, tol, max_iter, omega)


main()
