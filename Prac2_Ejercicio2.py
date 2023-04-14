import numpy as np
import matplotlib.pyplot as plt

# Dibujar la función exp(x) usando su polinomio de Taylor
def funExp(x0, tol=1.e-8, maxNumSum=100):
    suma = 0.
    error = np.inf
    iteraciones = 0
    factorial = 1.    
    while (error > tol and iteraciones < maxNumSum):
        termino = x0**iteraciones/factorial
        suma += termino
        error = np.max(termino)    
        iteraciones += 1
        factorial *= iteraciones
    return suma

f = lambda x: np.exp(x)
x = np.linspace(-1,1)
y = funExp(x)
plt.figure()
plt.plot(x,f(x),'y', linewidth = 4,label = 'f')
plt.plot(x,y,'b--',label = 'Aproximación f')
plt.plot(x,x*0,'k')    
plt.legend()
plt.title('Aproximación de f con el polinomio de McLaurin')
plt.show()