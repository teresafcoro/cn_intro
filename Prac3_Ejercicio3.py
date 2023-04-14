import numpy as np
np.set_printoptions(suppress = True)

# Ejercicio 1
def horner(p,x0):
    n = len(p)
    q = np.zeros(n)    
    q[0] = p[0]
    for i in range(1,n):
        q[i] = q[i-1]*x0 + p[i]        
    cociente = q[:-1]
    resto = q[-1]    
    return cociente, resto

def derPol(p,x0):
    derivadas = np.zeros_like(p)
    c = np.copy(p)
    factorial = 1.
    for i in range(len(c)):  
        c, r = horner(c,x0)
        derivadas[i] = r*factorial
        factorial *= i+1
    return derivadas    

p = np.array([1., -1, 2, -3,  5, -2])
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x0 = 1.
x1 = -1.
print('Derivadas sucesivas de P en x0 = 1')    
print(derPol(p,x0)) 
print('\n')
print('Derivadas sucesivas de R en x1 = -1')
print(derPol(r,x1))