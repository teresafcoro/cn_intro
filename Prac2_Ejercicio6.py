import numpy as np
import matplotlib.pyplot as plt
import math

def funTanh(x, tol=1.e-8):
    co = 1.
    si = x
    t = np.zeros(len(x))
    tant = si/co + 1
    error = 1.
    k = 0
    while error > tol:
        k += 1
        co += x**(2*k)/(math.factorial(2*k))
        si += x**(2*k+1)/(math.factorial(2*k+1))
        t += si/co
        error = np.max(t-tant)
        tant = t
    return t

f = lambda x: np.tanh(x)
x = np.linspace(-3, 3)
y = funTanh(x)
plt.figure()
plt.plot(x, f(x), 'y', linewidth = 4, label = 'f')
plt.plot(x, y, 'b--', label = 'Aproximación f')
plt.plot(x, x*0,'k-')    
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()