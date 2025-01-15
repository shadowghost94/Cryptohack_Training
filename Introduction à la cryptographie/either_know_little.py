from pwn import xor

cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytes.fromhex(cipher)

partial_key = xor(cipher_bytes[:7], "crypto{").decode()+'y'
complete_key = (partial_key * (len(cipher_bytes)//len(partial_key)+1))[:len(cipher_bytes)]

flag = xor(cipher_bytes, complete_key)

print(flag)
