import requests

def strxor(a, b):
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def get_flag_enc():
	r = requests.get(url+'ecbcbcwtf/encrypt_flag/')
	a = r.json()
	iv = a['ciphertext'].decode('hex')[:16]
	ciphertext = a['ciphertext'].decode('hex')[16:]
	return iv, ciphertext

def get_plaintext_ecb(ciphertext):
	r = requests.get(url+'ecbcbcwtf/decrypt/'+ciphertext+'/')
	a = r.json()
	p_0 = a['plaintext'].decode('hex')[:16]
	p_1 = a['plaintext'].decode('hex')[16:]

	return p_0, p_1

url = 'http://aes.cryptohack.org/'

iv, cipher = get_flag_enc()
c_hex = cipher.encode('hex')
p_0, p_1 = get_plaintext_ecb(c_hex)

actual1 = strxor(iv, p_0)
actual2 = strxor(cipher[:16], p_1)

print (actual1+actual2)
print (p_1.encode('hex'))
