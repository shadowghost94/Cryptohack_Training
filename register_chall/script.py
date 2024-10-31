def decrypt_caesar(ciphertext):
    for shift in range(0, 26):
        decrypted_message = ''
        for char in ciphertext:
            if char.isalpha():  # Vérifie si le caractère est une lettre
                # Gère le décalage pour les lettres majuscules et minuscules
                start = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr(start + (ord(char) - start - shift) % 26)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char  # Garde les caractères non alphabétiques inchangés

        print(f'Décalage {shift}: {decrypted_message}')

# Exemple d'utilisation
ciphertext = "YORQ YKSOTGX LOTMKX XKZAXT"
decrypt_caesar(ciphertext)
