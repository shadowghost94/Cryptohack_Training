from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

N = 882564595536224140639625987659416029426239230804614613279163

#prime factors
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

#public key
e = 65537

#euler totient
phi = (p-1)*(q-1)

#ciphertext
c = 77578995801157823671636298847186723593814843845525223303932

#private_key
d = mod_inverse(e, phi)

plaintext = pow(c, d, N)
print(long_to_bytes(plaintext))
