import numpy as np

# Ejercicio 1
def horner(p, x0):
    n = len(p)
    q = np.zeros_like(p)
    for i in range(n):
        q[i] = p[i]+q[i-1]*x0
    return q[:-1], q[-1]

# Ejercicio 4a
def divisores(m):
    div = np.zeros(2*m)
    count = 0
    for i in range(1, m+1):
        if np.remainder(m, i) == 0:
            div[count] = i
            div[count+1] = -i
            count +=2
    return div[:count]

def raices(p):
    r = np.zeros_like(p)
    m = abs(int(p[-1]))
    div = divisores(m)
    cont = 0
    i = 0
    x0 = div[i]
    while len(p) > 1:        
        q, resto = horner(p, x0)
        if resto == 0:
            r[cont] = x0
            cont += 1
            p = q
        else:
            i += 1
            x0 = div[i]
    return r[:cont]

p1 = np.array([1., -5, 1, 17, -22, 8])
p2 = np.array([1., -6, -9, 140, -369, 378, -135])
p3 = np.array([1., 0, -24, -30, 135, 366, 320, 96])   
p4 = np.array([1., -6, -26, 148, -59, -350, 156, 280])

print("Raices de p1 = ", raices(p1))
print("Raices de p2 = ", raices(p2))
print("Raices de p3 = ", raices(p3))
print("Raices de p4 = ", raices(p4))