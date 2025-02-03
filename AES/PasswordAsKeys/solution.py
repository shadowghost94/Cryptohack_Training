from Crypto.Cipher import AES
import hashlib

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

with open("words") as f:
    words = [w.strip() for w in f.readlines()]
    for w in words:
        key = hashlib.md5(w.encode()).digest()
        y = decrypt(ciphertext, key.hex()).decode('utf-8', errors='ignore')
        print(y)
