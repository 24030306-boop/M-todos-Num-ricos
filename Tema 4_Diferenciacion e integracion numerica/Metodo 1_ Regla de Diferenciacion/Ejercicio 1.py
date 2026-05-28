import math

def P(z):
    return math.exp(-0.5 * z) * math.sin(2 * z)

z0 = 0.8
h = 0.01

grad_aprox = (P(z0 + h) - P(z0 - h)) / (2 * h)

# Derivada exacta: P'(z) = e^(-0.5z)[2cos(2z) - 0.5sen(2z)]
grad_exacto = math.exp(-0.5*z0) * (2*math.cos(2*z0) - 0.5*math.sin(2*z0))
error_rel = abs(grad_aprox - grad_exacto) / abs(grad_exacto) * 100

print(f'Gradiente aproximado : {grad_aprox:.10f} Pa/m')
print(f'Gradiente exacto     : {grad_exacto:.10f} Pa/m')
print(f'Error relativo       : {error_rel:.6e} %')
