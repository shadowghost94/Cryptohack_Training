from sympy import isprime
import sys

a = 66528
b = 52920
container = []
fixeur = 0

if isprime(a) and isprime(b):
    print(f"pgcd de {a} et {b} est 1")
    sys.exit()

def superieur():
    if a<b:
        return a
    elif a>b:
        return b
    else:
        return a

x = superieur()

for i in range(x):
    if (i%2 == 0):
        container.append(i)

print(container)

for j in range(len(container)):
    if j > fixeur:
        fixeur = j

print(f"pgcd de {a} et {b} est {fixeur}")

# Re-importing the math module after environment reset
# import math
#
# # Given values
# a = 66528
# b = 52920
#
# # Calculate gcd(a, b)
# gcd_ab = math.gcd(a, b)
# gcd_ab

#Méthode 2
# def pgcd_euclide(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# # Exemple d'utilisation
# a = 66528
# b = 52920
# pgcd = pgcd_euclide(a, b)
# print(f"Le PGCD de {a} et {b} est {pgcd}")

#Méthode3
# def diviseurs(n):
#     return [i for i in range(1, n + 1) if n % i == 0]
#
# def pgcd_par_diviseurs(a, b):
#     div_a = diviseurs(a)
#     div_b = diviseurs(b)
#
#     # Trouver les diviseurs communs
#     div_commun = set(div_a) & set(div_b)
#
#     # Renvoyer le plus grand diviseur commun
#     return max(div_commun)
#
# # Exemple d'utilisation
# a = 66528
# b = 52920
# pgcd = pgcd_par_diviseurs(a, b)
# print(f"Le PGCD de {a} et {b} est {pgcd}")
