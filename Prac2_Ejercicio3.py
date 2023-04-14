import numpy as np
 
f = lambda x: np.sin(x)
x0 = np.pi/4
suma = 0.
error = np.inf
iteraciones = 1
iterAux = 1
factorial = 1.
while (error > 1.e-8 and iteraciones < 100):
    if (iteraciones % 2 != 0):
        termino = x0**iteraciones/factorial
        if (iterAux % 2 != 0):
            suma += termino
        else:
            suma -= termino
        iterAux += 1
        error = abs(termino)        
    iteraciones += 1
    factorial *= iteraciones

print('Valor aprox = ', suma)
print('Valor exacto = ', f(x0))
print('Número de iteraciones = ', iterAux-1)    # porque empiezo en uno