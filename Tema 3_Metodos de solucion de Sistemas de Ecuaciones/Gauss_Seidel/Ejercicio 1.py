def Gseid(a, b, n, x, imax, es, lmbda):
    for i in range(n):
        dummy = a[i][i]
        for j in range(n):
            a[i][j] = a[i][j] / dummy
        b[i] = b[i] / dummy

    for i in range(n):
        suma = b[i]
        for j in range(n):
            if i != j:
                suma = suma - a[i][j] * x[j]
        x[i] = suma

    iter = 1
    while True:
        centinela = 1
        for i in range(n):
            old = x[i]
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma = suma - a[i][j] * x[j]
            x[i] = lmbda * suma + (1.0 - lmbda) * old
            if centinela == 1 and x[i] != 0:
                ea = abs((x[i] - old) / x[i]) * 100
                if ea > es:
                    centinela = 0
        iter = iter + 1
        if centinela == 1 or iter >= imax:
            break

    return x, iter
