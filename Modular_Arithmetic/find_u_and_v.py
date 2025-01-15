# Re-import necessary modules after reset
import math

# Given values
p = 26513
q = 32321

# Implementing the extended Euclidean algorithm to find integers u and v such that p*u + q*v = gcd(p, q)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, u1, v1 = extended_gcd(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return gcd, u, v

# Calculate gcd and coefficients u, v
gcd_pq, u, v = extended_gcd(p, q)
print(gcd_pq, u, v)
