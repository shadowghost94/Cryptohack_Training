#le script suivant utilise la fonction python chr() pour convertir
#les codes ascii en lettre lisible
#l'inverse de chr() est ord() qui permet de trouver l'ascii correspondant à une lettre
contenant = ''
code_ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for x in code_ascii:
    contenant += chr(x)

print(contenant)
