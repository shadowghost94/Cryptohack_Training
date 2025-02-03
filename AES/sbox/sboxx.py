# Définition des coefficients hexadécimaux pour la fonction f(x)
coefficients = [0x05, 0x09, 0xF9, 0x25, 0xF4, 0x01, 0xB5, 0x8F, 0x63]

# Choisir un x au hasard dans GF(2^8)
x = 0x1A  # Exemple de valeur (26 en décimal)

# Calcul de f(x) dans GF(2^8)
def gf_mult(a, b):
    """Multiplication dans le champ fini GF(2^8) avec le polynôme irréductible x^8 + x^4 + x^3 + x + 1."""
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF  # Assure que le résultat est dans 8 bits
        if high_bit_set:
            a ^= 0x1B  # Réduction modulaire par le polynôme x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return p

# Calcul du polynôme f(x)
fx = 0
exponents = [0xFE, 0xFD, 0xFB, 0xF7, 0xEF, 0xDF, 0xBF, 0x7F]  # Exposants en hexadécimal
for coeff, exp in zip(coefficients[:-1], exponents):  # Ne pas inclure le dernier terme constant ici
    fx ^= gf_mult(coeff, x)  # Multiplication dans GF(2^8)

# Ajouter le terme constant (dernier coefficient)
fx ^= coefficients[-1]

fx
