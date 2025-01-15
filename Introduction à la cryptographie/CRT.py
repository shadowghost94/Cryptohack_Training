from math import gcd

def mod_inverse(a, m):
    # Algorithme d'Euclide étendu pour trouver l'inverse modulaire
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chinese_remainder_theorem(a, n):
    N = 1
    for ni in n:
        N *= ni

    x = 0
    for ai, ni in zip(a, n):
        Ni = N // ni
        Mi = mod_inverse(Ni, ni)
        x += ai * Mi * Ni
    return x % N

# Exemple
a = [2, 3, 5]  # Les restes
n = [5, 11, 17]  # Les modulos
solution = chinese_remainder_theorem(a, n)
print(f"La solution est x ≡ {solution}")
