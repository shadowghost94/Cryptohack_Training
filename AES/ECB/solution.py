#!/usr/bin/env python
"""
Author: Luke Spademan
License: MIT
Solves: https://aes.cryptohack.org/ecb_oracle/
Desc:
    The server returns aes_ebc(our_input + flag).
    We can manipute our input to work out the flag.
    EBC splits the input into blocks and encrypts each block in the same way.
    say the flag is crypto{secret_flag}.
    If our input was "A" * 16, the blocks would be
       AAAAAAAAAAAAAAAA
       crypto{secret_fl
       ag}
    To guess the first letter of the flag, we can make
    our input "A" * 15 + guess + "A" * 15.
    If our guess was "b", the blocks would be
       AAAAAAAAAAAAAAAb
       AAAAAAAAAAAAAAAc
       rypto{secret_fla
       g}
    We can then compare the output blocks and would see that they do not
    match, so the first letter of the flag is not "b".
    If we guessed "c", the blocks would be
       AAAAAAAAAAAAAAAc
       AAAAAAAAAAAAAAAc
       rypto{secret_fla
       g}
    The output blocks for the first two would match, so we would know
    "c" is the first letter of the flag.
    We can then try and guess the next letter. We know the first letter
    is "c" so to see if letter two is "a" we would make our input
    "A" * 14 + "ca" + "A" * 14. This would make the blocks
       AAAAAAAAAAAAAAca
       AAAAAAAAAAAAAAcr
       ypto{secret_flag
       }
    Again, we would see that this is wrong. We could itterate through each
    possible char until it matches, then move onto the third letter of the
    flag.
"""
import codecs
import requests


def encrypt(plaintext):
    plain_hex = plaintext.encode().hex()
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + plain_hex
    r = requests.get(url)
    r_data = r.json()
    return r_data.get("ciphertext", None)


def pad_flag_guess(guess):
    """
    Pads the text so that it can be compared with the start of the flag.
    i.e.
    pad_flag_guess("crypt") => AAAAAAAAAAAcrypt
                               AAAAAAAAAAA
    so that when the flag (e.g. crypto{secret_flag} is added by the server
        AAAAAAAAAAAcrypt
        AAAAAAAAAAAcrypt
        o{secret_flag}
    will be what is encrypted, meaning we can compare output blocks.
    """

    padding = "A" * (16 - len(guess) % 16)
    padded_guess = padding + guess + padding

    return padded_guess


if __name__ == "__main__":
    letters = "abcdefghijklmnopqrstuvwxyz1234567890_{}"
    flag = ""

    while flag[-1:] != "}":  # we know the flag ends with a '}'.
        for l in letters:
            flag_guess = flag + l
            padded_guess = pad_flag_guess(flag_guess)
            #ciphertext = encrypt(padded_guess)
            ciphertext = "f327d4f7aa8926e954dd3f29d791f77b8e99fa5be5828d03b4dda5c8fa56b0c45600414fa81b669b70704fba789076d8"

            guess_output_size = 2 * ((16 - len(flag_guess) % 16) + len(flag_guess))

            encrypted_guess = ciphertext[:guess_output_size]
            encrypted_flag = ciphertext[guess_output_size:guess_output_size*2]
            if encrypted_guess == encrypted_flag:
                flag = flag_guess
                print(l, end="", flush=True)  # print letter just guessed
                break
    print()  # print newline
