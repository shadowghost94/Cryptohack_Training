from pwn import xor

cipher = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')


for i in range(100):
    print(f"{i}\n")
    response = xor(cipher, i)
    print(response.decode())
