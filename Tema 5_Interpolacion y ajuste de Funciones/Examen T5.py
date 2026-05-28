#datos
x0 = 40.0
y0 = 12.0

x1 = 80.0
y1 = 20.93

x2 = 120.0
y2 = 14.0

x = 90.0

#Metodo de lagrange
arriba_0 = (x- x1) * (x - x2)
abajo_0 = (x0 - x1) * (x0 - x2)
l0 = arriba_0 / abajo_0

a1 = (x - x0) * (x - x2)
ab1 = (x1 - x0) * (x1 - x2)
l1 = a1/ ab1

a2 = (x- x0) * (x - x1)
ab2 = (x2 - x0) * (x2 - x1)
l2 = a2/ ab2


# resultado de y
r1 = y0 * l0
r2 = y1 * l1
r3 = y2 * l2

y = r1+r2+r3

print("Velocidad:", x)
print("Rendimiento:", y)