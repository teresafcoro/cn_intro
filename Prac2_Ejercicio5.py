import numpy as np
import math

x = 0.5
co = 1.
si = x
tant = si/co + 1
error = 1.
k = 0
while error > 1.e-4:
    k += 1
    co += x**(2*k)/(math.factorial(2*k))
    si += x**(2*k+1)/(math.factorial(2*k+1))
    t = si/co
    error = abs(t-tant)
    tant = t

print('Valor aprox  = ', t)
print('Valor exacto = ', np.tanh(x))