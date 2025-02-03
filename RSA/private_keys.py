from sympy import mod_inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

phi = (p-1) * (q-1)
e = 65537

d = mod_inverse(e, phi)
y = (e**(-1))%phi
print(d)
print(y)
