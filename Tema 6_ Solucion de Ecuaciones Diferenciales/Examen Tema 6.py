# Metodo de Euler 
def f(T):
    return -0.1 * (T - 20)
t = 0
T = 80
h = 0.5
tf = 1.5

print("Iteracion\t t\t T\t\t f(T)")
i = 0

while t < tf:

    pendiente = f(T)

    print(i, "\t\t", round(t,2), "\t", round(T,2), "\t", round(pendiente,4))
    T = T + h * pendiente
    t = t + h
    i += 1

print("\nTemperatura aproximada en t =", tf, "es:", round(T,2), "°C")