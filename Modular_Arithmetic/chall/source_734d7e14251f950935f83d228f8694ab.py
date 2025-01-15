from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    #pour chaque i, on convertit en binaire, chaque binaire aura un prefix Ob, [2:] pour supprimer les deux premiers caractères
    #zfill(8) permet de compléter le reste du binaire pour qu'elle fasse 8 octets
    #former un tableau d'éléments avec les 8 octest de chaque caractère de FLAG
    #mettre ensemble chaque éléments du tableau pour former un mot
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))
