# 6. Conversión Estrecha (Narrowing Primitive Conversion)
import ctypes

valor_double = 3.14159e10

# Python int() no desborda (es de precisión arbitraria)
valor_int_python = int(valor_double)
print(f"Valor Original:          {valor_double}")
print(f"int() en Python:         {valor_int_python}")
print("(Python no tiene overflow en int — precisión arbitraria)")

# Simulación del comportamiento de C con ctypes (int de 32 bits)
valor_c_int = ctypes.c_int32(int(valor_double)).value
print(f"\nSimulación C int32:      {valor_c_int}")
print("(Mismo resultado que C: overflow con signo negativo)")
