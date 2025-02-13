from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image
import numpy as np
import os

# Charger l'image
image_path = "kregan.jpg"
img = Image.open(image_path)

# Convertir l'image en octets
img_data = np.array(img)
img_bytes = img_data.tobytes()

# Générer une clé AES (16, 24 ou 32 octets)
key = os.urandom(16)  # Clé secrète aléatoire de 16 octets
iv = os.urandom(16)  # IV aléatoire pour le mode CBC

# Chiffrer avec AES-CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))

# Convertir le résultat chiffré en image
ciphered_array = np.frombuffer(ciphered_bytes[:len(img_bytes)], dtype=np.uint8)
ciphered_array = ciphered_array.reshape(img_data.shape)

# Sauvegarder et afficher l'image chiffrée
encrypted_img = Image.fromarray(ciphered_array)
encrypted_img.save("encrypted_image.jpg")
#encrypted_img.show()
