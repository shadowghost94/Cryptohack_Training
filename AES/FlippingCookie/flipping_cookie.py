from Crypto.Cipher import AES
from pwn import xor
import requests

bloc = []

def get_cookie():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    response = requests.get(url)
    return response.json()['cookie']

def check_admin(cookie, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/"+cookie+"/"+iv+"/"
    response = requests.get(url)
    return response

cookie = "4d21a54acbaf7353a2df5b3fe4bcfbed284312bf6e93be0a0b5f7d0fe4d810c59bf67f0684cd012b614be72020366cd9"
bloc = [cookie[i:i+32] for i in [0,32,64]]

# Dans le code ci-dessous, on saute juste le dernier parceque lui seul n'est pas utilisé dans le processus de xor
iv = bloc[0:(len(bloc)-1)]

for x in range(len(bloc)-1):
    bloc[x] = check_admin(cookie[x], iv[x])

for i in range(len(bloc)):
