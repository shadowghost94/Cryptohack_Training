from Crypto.Util.number import long_to_bytes

plaintext = "7b25db75e990ab4b5dd375de97e29f349055ad87dee65dda37bf601ca2f29c4ed1ad8c6bd4e6d232838284e9db7791b9"
plaintext_int = int(plaintext, 16)
print(long_to_bytes(plaintext_int))
