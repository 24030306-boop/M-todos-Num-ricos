def trapecio_datos(lecturas, delta_t):
    m    = len(lecturas)
    acum = (lecturas[0] + lecturas[-1]) / 2
    for j in range(1, m - 1):
        acum += lecturas[j]
    return acum * delta_t

irradiancia = [120, 340, 680, 820, 750, 410]
energia_total = trapecio_datos(irradiancia, 2)
print(f'Energía solar total: {energia_total:.2f} Wh/m²')

