# Modelo Lotka-Volterra con método de Heun
a, b, c, d = 1.0, 0.1, 1.5, 0.075

def sistema(t, x, y):
    return a*x - b*x*y, -c*y + d*x*y

def heun_sistema(t0, x0, y0, h, n):
    t, x, y = t0, x0, y0
    hist = [(t, x, y)]
    for _ in range(n):
        k1x, k1y = sistema(t, x, y)
        xp = x + h * k1x
        yp = y + h * k1y
        k2x, k2y = sistema(t + h, xp, yp)
        x = x + (h/2) * (k1x + k2x)
        y = y + (h/2) * (k1y + k2y)
        t += h
        hist.append((t, x, y))
    return hist

hist = heun_sistema(0, 10, 5, 0.1, 150)

print(f"{'t':>5} {'Presas':>10} {'Depredadores':>14}")
for t, x, y in hist[::15]:
    print(f"{t:5.1f} {x:10.4f} {y:14.4f}")
