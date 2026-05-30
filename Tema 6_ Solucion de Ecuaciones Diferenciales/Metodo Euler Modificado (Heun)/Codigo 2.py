# dy/dx = x*y^2 - y,  y(0) = 1
def f(x, y):
    return x * y**2 - y

def heun(f, x0, y0, h, x_final):
    x, y = x0, y0
    pasos = []
    while x <= x_final + 1e-9:
        k1 = f(x, y)
        y_pred = y + h * k1
        k2 = f(x + h, y_pred)
        prom = (k1 + k2) / 2
        pasos.append({'x': x, 'y': y,
                      'k1': k1, 'k2': k2, 'prom': prom})
        y = y + h * prom
        x = round(x + h, 10)
    return pasos

res = heun(f, x0=0, y0=1, h=0.1, x_final=1)

print(f"{'x':>5} {'y':>10} {'k1':>10} {'k2':>10} {'prom':>10}")
for p in res:
    print(f"{p['x']:5.2f} {p['y']:10.6f} {p['k1']:10.6f} {p['k2']:10.6f} {p['prom']:10.6f}")
