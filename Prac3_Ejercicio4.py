import numpy as np

# Ejercicio 1
def horner(p, x0):
    n = len(p)
    q = np.zeros_like(p)
    for i in range(n):
        q[i] = p[i]+q[i-1]*x0
    return q[:-1], q[-1]

# Apartado a
def divisores(m):
    div = np.zeros(2*m)
    count = 0
    for i in range(1, m+1):
        if np.remainder(m, i) == 0:
            div[count] = i
            div[count+1] = -i
            count +=2
    return div[:count]

print("Divisores de 6 = ", divisores(6))
print("Divisores de 6 = ", divisores(18))
print("Divisores de 6 = ", divisores(20))

# Apartado b
def raices(p):
    r = np.zeros_like(p)
    m = abs(int(p[-1]))
    div = divisores(m)
    cont = 0
    for x0 in div:
        q, resto = horner(p, x0)
        if resto == 0:
            r[cont] = x0
            cont += 1
            p = q
    return r[:cont]

p0 = np.array([1., 0, -1])
p1 = np.array([1., -3, -6, 8])
p2 = np.array([1., 2, -16, -2, 15])
p3 = np.array([1.,-5, -13, 53, 60])   
p4 = np.array([1., 4, -56, -206, 343, 490])

print("Raices de p0 = ", raices(p0))
print("Raices de p1 = ", raices(p1))
print("Raices de p2 = ", raices(p2))
print("Raices de p3 = ", raices(p3))
print("Raices de p4 = ", raices(p4))