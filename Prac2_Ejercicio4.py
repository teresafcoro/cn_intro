import numpy as np
import matplotlib.pyplot as plt       

def funSin(x0, tol=1.e-8, maxNumSum=100):
    suma = 0.
    error = np.inf
    iteraciones = 1
    iterAux = 1
    factorial = 1.
    while (error > tol and iteraciones < maxNumSum):
        if (iteraciones % 2 != 0):
            termino = x0**iteraciones/factorial
            if (iterAux % 2 != 0):
                suma += termino
            else:
                suma -= termino
            iterAux += 1           
            error = np.max(termino)        
        iteraciones += 1
        factorial *= iteraciones
    return suma

f = lambda x: np.sin(x)
x = np.linspace(-np.pi, np.pi)
y = funSin(x)
plt.figure()
plt.plot(x, f(x), 'y', linewidth = 4, label = 'f')
plt.plot(x, y, 'b--', label = 'Aproximación f')
plt.plot(x, x*0,'k')    
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()